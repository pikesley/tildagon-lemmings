import json

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


class Lemming:
    """A little guy."""

    def __init__(self, variety, params):
        """Construct."""
        self.conf = conf
        self.params = dict(defaults, **params)
        self.variety = variety

        self.flipped = self.params["flipped"]
        self.asset_path = self.params["asset-path"]
        self.scale = self.params["scale"]
        self.speed = self.params["speed"]
        self.moonwalker = self.params["moonwalker"]

        # if self.params["randomised-offset"]:
        #     self.randomise_offset()

        self.load_frames()
        self.frame_index = 0
        self.opacity = 1

        self.hue = params.get("hue", 1.0)

        self.outfit = RotatingOutfit(self.hue)

    def load_frames(self):
        """Load frames."""
        source = self.variety

        # XOR these two
        if self.flipped != self.moonwalker:
            source = f"{self.variety}-flipped"

        self.frames = json.loads(
            open(self.asset_path + f"bitmaps/{source}.json").read()
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
