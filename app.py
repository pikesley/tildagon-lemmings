import gzip
import json
import os
from events.input import BUTTON_TYPES, Buttons
from system.eventbus import eventbus
from system.patterndisplay.events import PatternDisable
from tildagonos import tildagonos

import app
from .lib.gamma import gamma_corrections

from .common.colour_tools import rgb_from_hue
from .common.shapes.square import Square
from .lib.asset_path import ASSET_PATH
from .lib.background import Background
from .lib.conf import conf


class Lemmings(app.App):
    """Lemmings."""

    def __init__(self):
        """Construct."""
        eventbus.emit(PatternDisable())
        self.button_states = Buttons(self)
        self.index = 0
        self.load_frames("walker")

        self.pixel_size = conf["pixel-size"]
        self.hue = 0.5

    def load_frames(self, lemming, zipped=False):
        """Load data."""
        self.sprites = []

        width = len(os.listdir(ASSET_PATH + f"bitmaps/{lemming}"))

        for i in range(width):
            data = None

            if zipped:
                data = json.loads(
                    gzip.decompress(
                        open(ASSET_PATH + f"bitmaps/{lemming}/{i}.json.gz", "rb").read()
                    ).decode()
                )
            else:
                data = json.loads(
                    open(ASSET_PATH + f"bitmaps/{lemming}/{i}.json").read()
                )

            self.sprites.append(data)



    def update(self, _):
        """Update."""
        self.scan_buttons()
        self.index = (self.index + 1) % len(self.sprites)
        self.hue = (self.hue + conf["hue-increment"]) % 1
        self.light_leds()

    def draw(self, ctx):
        """Draw."""
        self.overlays = []
        self.overlays.append(Background(colour=(0, 0, 0)))
        # self.overlays.append(Background(colour=rgb_from_hue(self.hue)))

        self.start_x = 0 - ((16 / 2) * self.pixel_size)
        self.start_y = 0 - ((len(self.sprites[0]) / 2) * self.pixel_size)

        for i, row in enumerate(self.sprites[self.index]):
            for j, item in enumerate(row):
                self.overlays.append(
                    Square(
                        centre=(
                            self.start_x + (j * (self.pixel_size)),
                            self.start_y + (i * (self.pixel_size)),
                        ),
                        colour=[x / 255 for x in item[0:3]],
                        size=self.pixel_size / 2,
                        opacity=item[-1],
                    )
                )
        self.draw_overlays(ctx)

    def scan_buttons(self):
        """Buttons."""
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()
            self.minimise()

    def light_leds(self):
        """Light the lights."""
        colour = rgb_from_hue(self.hue + 0.5)
        for i in range(18):
            if i > 11:
                colour = rgb_from_hue(self.hue)
            tildagonos.leds[i+1] = [gamma_corrections[int(i * 255 * conf["led-brightness"])] for i in colour]

        tildagonos.leds.write()
__app_export__ = Lemmings
