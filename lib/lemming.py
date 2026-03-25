import gzip
import json
import os

try:
    from ..common.shapes.square import Square
except ImportError:
    from common.shapes.square import Square

try:  # noqa: SIM105
    from .asset_path import ASSET_PATH
except FileNotFoundError:
    pass

from .sprite_flipper import flip_sprite


class Lemming:
    """A little guy."""

    def __init__(  # noqa: PLR0913
        self,
        variety,
        scale=5,
        speed=1,
        flipped=False,
        asset_path=None,
        compressed_bitmaps=True,
    ):
        """Construct."""
        self.variety = variety
        self.flipped = flipped
        self.asset_path = asset_path or ASSET_PATH
        self.compressed_bitmaps = compressed_bitmaps
        self.scale = scale
        self.speed = speed

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
            self.height = len(self.frames)

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
