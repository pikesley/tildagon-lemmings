import json

try:
    from .asset_path import ASSET_PATH
except FileNotFoundError:
    ASSET_PATH = ""


defaults = {
    "scale": 4,
    "speed": 1,
    "flipped": False,
    "asset-path": ASSET_PATH,
    "compressed-bitmaps": True,
}

colours = {
    "background": [1, 0, 1],
    "hair": [0.0, 0.7019607843137254, 0.0],
    "flesh": [1.0, 0.9215686274509803, 0.8745098039215686],
    "clothing": [0.37254901960784315, 0.38823529411764707, 1.0],
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
        source = self.variety
        if self.flipped:
            source = f"{source}-flipped"

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
                opacity = 1
                if item == "background":
                    opacity = 0
                pix.append(
                    Pixel(
                        start_x + (j * self.scale),
                        start_y + (i * self.scale),
                        self.scale,
                        colours[item],
                        opacity,
                    )
                )

        return pix


class Pixel:
    """A square."""

    def __init__(self, left, top, size, colour, opacity):
        """Construct."""
        self.left = left
        self.top = top
        self.size = size
        self.colour = list(colour) + [opacity]

    def draw(self, ctx):
        """Draw."""
        ctx.rgba(*self.colour)

        ctx.rectangle(
            self.left,
            self.top,
            self.size,
            self.size,
        )

        ctx.fill()
