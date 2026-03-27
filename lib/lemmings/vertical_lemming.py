from math import sqrt
from random import randint

from ..lemming import Lemming


class VerticalLemming(Lemming):
    """An up-down lemming."""

    def __init__(self, variety, params):
        """Construct."""
        super().__init__(variety, params)

        self.x = 0
        self.x_limit = 120 - ((self.width / 2) * self.scale)

        if self.params["randomised-offset"]:
            self.randomise_offset()

        self.y = self.calculate_start_y()
        self.final_y = 0 - self.y

    def calculate_start_y(self):
        """Starting y-position."""
        limit = sqrt(120**2 - self.x**2)

        position = -limit - (self.height * self.scale)

        return round(position)

    @property
    def done(self):
        """Are we off-screen?"""
        return self.y > self.final_y

    def set_x(self, value):
        """Set our `x`."""
        self.x = value
        self.y = self.calculate_start_y()
        self.final_y = 0 - self.y

    def randomise_offset(self):
        """Set x to something random."""
        self.set_x(randint(int(-self.x_limit), int(self.x_limit)))
