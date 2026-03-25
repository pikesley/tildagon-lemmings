from random import randint

from ..lemming import Lemming


class HorizontalLemming(Lemming):
    """A walking lemming."""

    def __init__(self, variety, params):
        """Construct."""
        super().__init__(variety, params)

        self.y = 0
        self.y_limit = 120 - (((self.height / 2) * self.scale) + (self.scale / 2))

        self.x = -120 - (len(self.frames[0]) * self.scale)
        if self.flipped:
            self.x = 120 + (len(self.frames[0]) * self.scale)

    @property
    def done(self):
        """Are we off-screen?"""
        if self.flipped:
            return self.x < -120 - (len(self.frames[0]) * self.scale)
        return self.x > 120

    def randomise_offset(self):
        """Set y to something random."""
        self.y = randint(int(-self.y_limit), int(self.y_limit))
