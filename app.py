from math import atan2
from random import choice, randint, random

import imu
from events.input import BUTTON_TYPES, Buttons
from system.eventbus import eventbus
from system.patterndisplay.events import PatternDisable
from tildagonos import tildagonos

import app

from .common.colour_tools import rgb_from_hue
from .common.map_value import map_value
from .lib.background import Background
from .lib.conf import conf
from .lib.gamma import gamma_corrections
from .lib.lemmings.walker import Walker

characters = [
    # Faller,
    Walker,
    # Basher,
]


class Lemmings(app.App):
    """Lemmings."""

    def __init__(self):
        """Construct."""
        eventbus.emit(PatternDisable())
        self.button_states = Buttons(self)
        self.index = 0

        self.hue = 1 / 3

        self.lemming_count = conf["lemming-count"]
        self.lemmings = [self.new_lemming() for i in range(self.lemming_count)]

        self.rotation_offset = 0

    def new_lemming(self):
        """New little guy."""
        params = {
            "scale": randint(conf["scale"]["min"], conf["scale"]["max"]) * 2,
            "flipped": choice([True, False]),
            "hue": self.hue,
        }
        if random() > conf["moonwalk-threshold"]:
            params["moonwalker"] = True
            params["hue"] = self.hue + 1 / 3

        lemming = choice(characters)(params)
        lemming.randomise_offset()
        lemming.opacity = map_value(
            lemming.scale, conf["scale"]["min"], conf["scale"]["max"], 0.2, 1
        )

        return lemming

    def update(self, _):
        """Update."""
        acc = imu.acc_read()
        weighting = min(1.0, int(abs(10 - acc[2])) / 9)
        self.rotation_offset = (atan2(acc[1], acc[0])) * weighting

        self.scan_buttons()
        for lemming in self.lemmings:
            lemming.animate()
            lemming.move()

        self.hue = (self.hue + conf["hue-increment"]) % 1
        self.light_leds()

        fresh_lemmings = []
        for lemming in self.lemmings:
            if not lemming.done:
                fresh_lemmings.append(lemming)  # noqa: PERF401

        for _ in range(self.lemming_count - len(fresh_lemmings)):
            fresh_lemmings.append(self.new_lemming())  # noqa: PERF401

        self.lemmings = sorted(fresh_lemmings)

    def draw(self, ctx):
        """Draw."""
        ctx.rotate(-self.rotation_offset)

        self.overlays = []
        self.overlays.append(Background(colour=(0, 0, 0)))

        for lemming in self.lemmings:
            self.overlays.extend(lemming.pixels)
        self.draw_overlays(ctx)

    def scan_buttons(self):
        """Buttons."""
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()
            self.minimise()

        if self.button_states.get(BUTTON_TYPES["UP"]):
            self.button_states.clear()
            self.next_lemming()

        if self.button_states.get(BUTTON_TYPES["RIGHT"]):
            self.button_states.clear()
            self.lemming.animate()
            print(self.lemming.frame_index)

        if self.button_states.get(BUTTON_TYPES["LEFT"]):
            self.button_states.clear()
            self.lemming.move()
            print(self.lemming.frame_index)

    def light_leds(self):
        """Light the lights."""
        colour = rgb_from_hue(self.hue)
        for i in range(18):
            if i > 11:
                colour = rgb_from_hue(self.hue + 1 / 3)
            tildagonos.leds[i + 1] = [
                gamma_corrections[int(i * 255 * conf["led-brightness"])] for i in colour
            ]

        tildagonos.leds.write()


__app_export__ = Lemmings
