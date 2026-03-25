import gzip
import json
import os

try:
    from ..common.shapes.square import Square
except ImportError:
    from common.shapes.square import Square

try:
    from .asset_path import ASSET_PATH
except FileNotFoundError:
    ASSET_PATH = ""

from .sprite_flipper import flip_sprite

defaults = {
    "scale": 4,
    "speed": 1,
    "flipped": False,
    "asset-path": ASSET_PATH,
    "compressed-bitmaps": True,
}


class Lemming:
    """A little guy."""

    def __init__(self, variety, params):
        """Construct."""
        self.params = dict(defaults, **params)
        self.variety = variety

        self.flipped = self.params["flipped"]
        self.asset_path = self.params["asset-path"]
        self.compressed_bitmaps = self.params["compressed-bitmaps"]
        self.scale = self.params["scale"]
        self.speed = self.params["speed"]

        self.load_frames()
        self.frame_index = 0

    def load_frames(self):
        """Load frames."""
        self.frames = []
        self.width = len(os.listdir(self.asset_path + f"bitmaps/{self.variety}"))

        for i in range(self.width):
            if self.compressed_bitmaps:
                data = json.loads(
                    gzip.decompress(
                        open(
                            self.asset_path + f"bitmaps/{self.variety}/{i}.json.gz",
                            "rb",
                        ).read()
                    ).decode()
                )
            else:
                data = json.loads(
                    open(self.asset_path + f"bitmaps/{self.variety}/{i}.json").read()
                )

            if self.flipped:
                data = flip_sprite(data)
            self.frames.append(data)

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
                pix.append(
                    Square(
                        centre=(
                            start_x + (j * (self.scale)),
                            start_y + (i * (self.scale)),
                        ),
                        # colour=[x / 255 for x in item[0:3]],
                        colour=item[0:3],
                        size=self.scale / 2,
                        opacity=item[-1],
                    )
                )

        return pix
