import gc

from events.input import BUTTON_TYPES, Buttons
from system.eventbus import eventbus
from system.patterndisplay.events import PatternDisable

import app

from .common.colour_tools import rgb_from_hue
from .common.led_lighter import LEDLighter
from .common.rotation_monitor import RotationMonitor
from .lib.background import Background
from .lib.colony import Colony
from .lib.conf import conf

DEBUG = None  # `None`, or a classname, e.g. "Pickaxe"


class Lemmings(app.App):
    """Lemmings."""

    def __init__(self):
        """Construct."""
        eventbus.emit(PatternDisable())
        self.button_states = Buttons(self)
        self.index = 0

        self.hue = 1 / 3
        self.colony = Colony(self.hue, conf, debug=DEBUG)

        self.rotation_monitor = RotationMonitor()
        self.leds = LEDLighter(conf["led-brightness"])

    def update(self, _):
        """Update."""
        self.scan_buttons()

        self.hue = (self.hue + conf["hue-increment"]) % 1
        self.leds.light(self.hue + 0.5, self.hue)

        self.colony.hue = self.hue
        self.colony.mobilise()
        self.colony.maintain()

        gc.collect()

    def draw(self, ctx):
        """Draw."""
        if not DEBUG:
            ctx.rotate(self.rotation_monitor.read())

        self.overlays = []
        self.overlays.append(Background(bottom_colour=rgb_from_hue(self.hue + 0.5)))

        for lemming in self.colony.lemmings:
            self.overlays.extend(lemming.pixels)

        self.draw_overlays(ctx)

    def scan_buttons(self):
        """Buttons."""
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()
            self.minimise()

        if self.button_states.get(BUTTON_TYPES["UP"]):
            self.button_states.clear()
            self.colony.dottify(True)

        if self.button_states.get(BUTTON_TYPES["DOWN"]):
            self.button_states.clear()
            self.colony.dottify(False)

        if self.button_states.get(BUTTON_TYPES["RIGHT"]):
            self.button_states.clear()
            if DEBUG:
                for lemming in self.colony.lemmings:
                    lemming.animate()

        if self.button_states.get(BUTTON_TYPES["LEFT"]):
            self.button_states.clear()
            if DEBUG:
                for lemming in self.colony.lemmings:
                    lemming.move()


__app_export__ = Lemmings
