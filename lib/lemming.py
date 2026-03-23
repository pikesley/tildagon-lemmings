import gzip
import json
import os

from ..common.shapes.square import Square
from .asset_path import ASSET_PATH
from .sprite_flipper import flip_sprite


class Lemming:
    """A little guy."""

    def __init__(self, y=-80, scale=5, speed=1, flipped=False):
        """Construct."""
        self.variety = "walker"
        self.flipped = flipped
        self.load_frames()
        self.scale = scale
        self.x = -120 - (len(self.frames[0]) * self.scale)
        if self.flipped:
            self.x = 120 + (len(self.frames[0]) * self.scale)

        self.y = y
        self.speed = speed

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

    @property
    def done(self):
        """Are we off-screen?"""
        if self.flipped:
            return self.x < -120 - (len(self.frames[0]) * self.scale)
        return self.x > 120

    def move(self):
        """Walk."""
        if self.flipped:
            self.x -= self.speed * self.scale
        else:
            self.x += self.speed * self.scale

    def animate(self):
        """Animate."""
        self.frames = self.frames[1:] + [self.frames[0]]

    @property
    def pixels(self):
        """Draw."""
        pix = []
        for i, row in enumerate(self.frames[0]):
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
