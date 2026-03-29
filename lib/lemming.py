import json
from math import sqrt
from random import randint

from .outfits import RotatingOutfit
from .pixel import Pixel

try:
    from .asset_path import ASSET_PATH
except FileNotFoundError:
    ASSET_PATH = ""

try:
    from .conf import conf
except FileNotFoundError:
    import json
    from pathlib import Path

    conf = json.loads(Path("conf.json").read_text())


defaults = dict(conf["lemming-defaults"], **{"asset-path": ASSET_PATH})

# for a HorizontalLemming, `fixed_position` == `y`, `variable_position` == `x`
# for a VerticalLemming, `fixed_position` == `x`, `variable_position` == `y`


class Lemming:
    """A little guy."""

    def __init__(self, params):
        """Construct."""
        # this is clunky
        self.subclass = self.__class__.__bases__[0].__name__

        # this allows us to test the intermediate classes
        if self.subclass == "Lemming":
            self.subclass = self.__class__.__name__

        # this is also purely for testing, real subclasses set their name
        if "name" in params:
            self.name = params["name"]

        self.conf = conf
        self.params = dict(defaults, **params)

        self.flipped = self.params["flipped"]
        self.asset_path = self.params["asset-path"]
        self.scale = self.params["scale"]
        self.speed = self.params["speed"]
        self.moonwalker = self.params["moonwalker"]

        self.load_frames()
        self.frame_index = 0

        self.configure()

    def configure(self):
        """Post-initialisation configuration."""
        if self.subclass == "HorizontalLemming":
            self.scaling_dimension = self.width
        else:
            self.scaling_dimension = self.height

        self.opacity = 1

        self.hue = self.params.get("hue", 1.0)

        self.outfit = RotatingOutfit(self.hue)

        # our starting `y`` (for Horizontal) or `x` (for Vertical)
        self.fixed_position = 0

        # ensure the entire lemming fits on the screen
        self.fixed_position_limit = 120 - ((self.scaling_dimension / 2) * self.scale)

        if self.params["randomised-offset"]:
            self.randomise_offset()

        # the axis we move through. `x` for Horizontal or `y` for Vertical
        self.variable_position = self.calculate_start_variable_position()
        self.final_variable_position = 0 - self.variable_position

    def load_frames(self):
        """Load frames."""
        source = "regular"

        # XOR these two
        if self.flipped != self.moonwalker:
            source = "inverted"

        self.frames = json.loads(
            open(self.asset_path + f"bitmaps/{self.name}/{source}.json").read()
        )

        self.width = len(self.frames[0][0])
        self.height = len(self.frames[0])

    def animate(self):
        """Animate."""
        self.frame_index = (self.frame_index + 1) % len(self.frames)

    @property
    def pixels(self):
        """Draw."""
        pix = []
        start_x = self.x - (self.width * self.scale / 2)
        start_y = self.y - (self.height * self.scale / 2)
        for i, row in enumerate(self.frames[self.frame_index]):
            for j, item in enumerate(row):
                opacity = self.opacity
                colour = self.outfit.get(item, (0, 0, 0))
                if item == "bg":
                    opacity = 0
                pix.append(
                    Pixel(
                        start_x + (j * self.scale),
                        start_y + (i * self.scale),
                        self.scale,
                        colour,
                        opacity,
                    )
                )

        return pix

    def __lt__(self, other):
        """Make us sortable."""
        return self.scale < other.scale

    @property
    def done(self):
        """Are we off-screen?"""
        if self.flipped:
            return self.variable_position < self.final_variable_position
        return self.variable_position > self.final_variable_position

    def set_fixed_position(self, value):
        """Set our `fixed_position`."""
        self.fixed_position = value
        self.variable_position = self.calculate_start_variable_position()
        self.final_variable_position = 0 - self.variable_position

    def randomise_offset(self):
        """Set `fixed_position` to something random."""
        self.set_fixed_position(
            randint(int(-self.fixed_position_limit), int(self.fixed_position_limit))
        )

    def calculate_start_variable_position(self):
        """Starting `variable_position`."""
        limit = sqrt(120**2 - self.fixed_position**2)

        position = -limit - (self.scaling_dimension * self.scale)
        if self.flipped and self.subclass == "HorizontalLemming":
            position = limit + (self.scaling_dimension * self.scale)

        return round(position)
