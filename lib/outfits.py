from random import choice

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


class Outfit:
    """Base class."""

    def __getitem__(self, key):
        """`foo[key]`."""
        return self.data[key]

    def get(self, key, default):
        """`foo.get(key)`."""
        if key in self.data:
            return self.data[key]
        return default


class RandomOutfit(Outfit):
    """Lemming clothes."""

    def __init__(self, _):
        """Construct."""
        self.colours = list(conf["colours"].values())
        self.keys = ["hair", "clothing"]

        self.data = dict(conf["default-colours"])
        for key in self.keys:
            self.data[key] = choice(self.colours)


class RotatingOutfit(Outfit):
    """Lemming clothes."""

    def __init__(self, hue):
        """Construct."""
        self.data = {
            "flesh": conf["default-colours"]["flesh"],
            "hair": rgb_from_hue(hue),
            "clothing": rgb_from_hue(hue + 1 / 3),
        }


class TriadicOutfit(Outfit):
    """Lemming clothes."""

    def __init__(self, hue):
        """Construct."""
        self.data = {
            "flesh": rgb_from_hue(hue),
            "hair": rgb_from_hue(hue + 1 / 3),
            "clothing": rgb_from_hue(hue + 2 / 3),
        }
