from random import choice, random

try:
    from ..common.map_value import map_value
except ImportError:
    from common.map_value import map_value

from .lemmings.faller import Faller
from .lemmings.walker import Walker


class Colony:
    """A group of lemmings."""

    def __init__(self, hue, conf):
        """Construct."""
        self.hue = hue
        self.conf = conf
        self.count = conf["lemming-count"]

        self.freak_token = 1

        self.scale_values = set(
            range(self.conf["scale"]["min"], self.conf["scale"]["max"] + 1)
        )
        self.lemmings = [self.new_lemming() for i in range(self.count)]

    def new_lemming(self):
        """New little guy."""
        scale = choice(tuple(self.scale_values))
        self.scale_values.remove(scale)

        params = {
            "scale": scale,
            "flipped": choice([True, False]),
            "hue": self.hue,
            "randomised-offset": True,
        }
        lemming_class = Walker
        if random() > self.conf["freak-threshold"] and self.freak_token:
            lemming_class = Faller
            self.freak_token = 0
            params["freak"] = True

        if lemming_class == Walker and random() > self.conf["moonwalk-threshold"]:
            params["moonwalker"] = True
            params["hue"] = self.hue + 1 / 3

        lemming = lemming_class(params)
        lemming.opacity = map_value(
            lemming.scale, self.conf["scale"]["min"], self.conf["scale"]["max"], 0.5, 1
        )

        return lemming

    def mobilise(self):
        """Move our lemmings."""
        for lemming in self.lemmings:
            lemming.animate()
            lemming.move()

    def maintain(self):
        """Ensure we have a full contingent."""
        fresh_lemmings = []
        for lemming in self.lemmings:
            if not lemming.done:
                fresh_lemmings.append(lemming)
            else:
                self.scale_values.add(lemming.scale)
                if "freak" in lemming.params:
                    self.freak_token = 1

        for _ in range(self.count - len(fresh_lemmings)):
            fresh_lemmings.append(self.new_lemming())  # noqa: PERF401

        self.lemmings = sorted(fresh_lemmings)
