from math import sqrt
from random import randint

from ..lemming import Lemming


class HorizontalLemming(Lemming):
    """A walking lemming."""

    def __init__(self, variety, params):
        """Construct."""
        super().__init__(variety, params)

        self.y = 0
        self.y_limit = 120 - ((self.height / 2) * self.scale)

        if self.params["randomised-offset"]:
            self.randomise_offset()

        self.x = self.calculate_start_x()
        self.final_x = 0 - self.x

    def calculate_start_x(self):
        """Starting x-position."""
        limit = sqrt(120**2 - self.y**2)

        position = -limit - (self.width * self.scale)
        if self.flipped:
            position = limit + (self.width * self.scale)

        return round(position)

    @property
    def done(self):
        """Are we off-screen?"""
        if self.flipped:
            return self.x < self.final_x
        return self.x > self.final_x

    def set_y(self, value):
        """Set our `y`."""
        self.y = value
        self.x = self.calculate_start_x()
        self.final_x = 0 - self.x

    def randomise_offset(self):
        """Set y to something random."""
        self.set_y(randint(int(-self.y_limit), int(self.y_limit)))
