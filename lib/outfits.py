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
            "sk": conf["default-colours"]["sk"],
            "hr": rgb_from_hue(hue),
            "cl": rgb_from_hue(hue + 1 / 3),
            "um": rgb_from_hue(hue + 2 / 3),
            "dt": rgb_from_hue(hue + 2 / 3),
        }

    def __getitem__(self, key):
        """`foo[key]`."""
        return self.data[key]

    def get(self, key, default):
        """`foo.get(key)`."""
        if key in self.data:
            return self.data[key]
        return default
