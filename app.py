from events.input import BUTTON_TYPES, Buttons
from system.eventbus import eventbus
from system.patterndisplay.events import PatternDisable

import app

from .common.led_lighter import LEDLighter
from .common.rotation_monitor import RotationMonitor
from .lib.background import Background
from .lib.colony import Colony
from .lib.conf import conf


class Lemmings(app.App):
    """Lemmings."""

    def __init__(self):
        """Construct."""
        eventbus.emit(PatternDisable())
        self.button_states = Buttons(self)
        self.index = 0

        self.hue = 1 / 3
        self.colony = Colony(self.hue, conf)

        self.rotation_monitor = RotationMonitor()
        self.leds = LEDLighter(conf["led-brightness"])

    def update(self, _):
        """Update."""
        self.scan_buttons()

        self.hue = (self.hue + conf["hue-increment"]) % 1
        self.leds.light(self.hue, self.hue + 1 / 3)

        self.colony.hue = self.hue
        self.colony.mobilise()
        self.colony.maintain()

    def draw(self, ctx):
        """Draw."""
        ctx.rotate(self.rotation_monitor.read())

        self.overlays = []
        self.overlays.append(Background(colour=(0, 0, 0)))

        for lemming in self.colony.lemmings:
            self.overlays.extend(lemming.pixels)
        self.draw_overlays(ctx)

    def scan_buttons(self):
        """Buttons."""
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()
            self.minimise()


__app_export__ = Lemmings
