try:
    from ..common.colour_tools import rgb_from_hue
except ImportError:
    from common.colour_tools import rgb_from_hue

try:
    from .conf import conf
except FileNotFoundError:
    import json
    from pathlib import Path

    conf = json.loads(Path("conf.json").read_text())


class RotatingOutfit:
    """Lemming clothes."""

    def __init__(self, hue):
        """Construct."""
        self.data = {
            "sk": conf["default-colours"]["skin"],  # skin
            "hr": rgb_from_hue(hue + conf["colour-offsets"]["hair"]),
            "cl": rgb_from_hue(hue + conf["colour-offsets"]["clothing"]),
            "um": rgb_from_hue(hue + conf["colour-offsets"]["umbrella"]),
            "dt": rgb_from_hue(hue + conf["colour-offsets"]["dirt"]),
        }

    def __getitem__(self, key):
        """`foo[key]`."""
        return self.data[key]

    def get(self, key, default):
        """`foo.get(key)`."""
        if key in self.data:
            return self.data[key]
        return default
