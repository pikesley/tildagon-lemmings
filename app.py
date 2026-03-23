from random import choice, randint

from events.input import BUTTON_TYPES, Buttons
from system.eventbus import eventbus
from system.patterndisplay.events import PatternDisable
from tildagonos import tildagonos

import app

from .common.colour_tools import rgb_from_hue
from .lib.background import Background
from .lib.conf import conf
from .lib.gamma import gamma_corrections
from .lib.lemming import Lemming


class Lemmings(app.App):
    """Lemmings."""

    def __init__(self):
        """Construct."""
        eventbus.emit(PatternDisable())
        self.button_states = Buttons(self)
        self.index = 0

        self.hue = 0.5
        self.lemming = Lemming(
            y=randint(-100, 100),
            scale=randint(conf["scale"]["min"], conf["scale"]["max"]) * 2,
            flipped=choice([True, False]),
        )

    def update(self, _):
        """Update."""
        self.scan_buttons()
        self.lemming.animate()
        self.lemming.move()
        self.hue = (self.hue + conf["hue-increment"]) % 1
        self.light_leds()
        if self.lemming.done:
            self.lemming = Lemming(
                y=randint(-100, 100),
                scale=randint(conf["scale"]["min"], conf["scale"]["max"]),
                flipped=choice([True, False]),
            )

    def draw(self, ctx):
        """Draw."""
        self.overlays = []
        self.overlays.append(Background(colour=(0, 0, 0)))

        self.overlays.extend(self.lemming.pixels)
        self.draw_overlays(ctx)

    def scan_buttons(self):
        """Buttons."""
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()
            self.minimise()

        if self.button_states.get(BUTTON_TYPES["UP"]):
            self.button_states.clear()
            self.next_lemming()

    def light_leds(self):
        """Light the lights."""
        colour = rgb_from_hue(self.hue + 0.5)
        for i in range(18):
            if i > 11:
                colour = rgb_from_hue(self.hue)
            tildagonos.leds[i + 1] = [
                gamma_corrections[int(i * 255 * conf["led-brightness"])] for i in colour
            ]

        tildagonos.leds.write()


__app_export__ = Lemmings
