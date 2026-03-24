import gzip
import json
import os

from ..common.shapes.square import Square
from .asset_path import ASSET_PATH
from .sprite_flipper import flip_sprite


class Lemming:
    """A little guy."""

    def __init__(self, variety, scale=5, speed=1, flipped=False):
        """Construct."""
        self.variety = variety
        self.flipped = flipped
        self.load_frames()
        self.scale = scale

        self.speed = speed

        self.frame_index = 0

    def load_frames(self):
        """Load frames."""
        self.frames = []
        width = len(os.listdir(ASSET_PATH + f"bitmaps/{self.variety}"))

        for i in range(width):
            data = json.loads(
                gzip.decompress(
                    open(
                        ASSET_PATH + f"bitmaps/{self.variety}/{i}.json.gz", "rb"
                    ).read()
                ).decode()
            )
            if self.flipped:
                data = flip_sprite(data)
            self.frames.append(data)


    def animate(self):
        """Animate."""
        self.frame_index = (self.frame_index + 1) % len(self.frames)

    @property
    def pixels(self):
        """Draw."""
        pix = []
        for i, row in enumerate(self.frames[self.frame_index]):
            for j, item in enumerate(row):
                pix.append(
                    Square(
                        centre=(
                            self.x + (j * (self.scale)),
                            self.y + (i * (self.scale)),
                        ),
                        colour=[x / 255 for x in item[0:3]],
                        size=self.scale / 2,
                        opacity=item[-1],
                    )
                )

        return pix
