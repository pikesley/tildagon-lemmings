from random import choice, randint, random

from ..common.map_value import map_value
from .lemmings.faller import Faller
from .lemmings.walker import Walker


class Colony:
    """A group of lemmings."""

    def __init__(self, hue, conf):
        """Construct."""
        self.hue = hue
        self.conf = conf
        self.count = conf["lemming-count"]

        self.lemmings = [self.new_lemming() for i in range(self.count)]

    def new_lemming(self):
        """New little guy."""
        params = {
            "scale": randint(self.conf["scale"]["min"], self.conf["scale"]["max"]) * 2,
            "flipped": choice([True, False]),
            "hue": self.hue,
            "randomised-offset": True,
        }
        if random() > self.conf["moonwalk-threshold"]:
            params["moonwalker"] = True
            params["hue"] = self.hue + 1 / 3

        lemming_class = Walker
        if random() > self.conf["faller-threshold"]:
            lemming_class = Faller

        lemming = lemming_class(params)
        lemming.opacity = map_value(
            lemming.scale, self.conf["scale"]["min"], self.conf["scale"]["max"], 0.2, 1
        )

        return lemming
