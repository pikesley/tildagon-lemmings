from math import sqrt
from random import randint

from ..lemming import Lemming


class HorizontalLemming(Lemming):
    """A walking lemming."""

    def __init__(self, params):
        """Construct."""
        super().__init__(params)

        self.fixed_position = 0
        self.fixed_position_limit = 120 - ((self.height / 2) * self.scale)
        self.y = self.fixed_position

        if self.params["randomised-offset"]:
            self.randomise_offset()

        self.x = self.calculate_start_x()
        self.final_x = 0 - self.x

    def calculate_start_x(self):
        """Starting x-position."""
        limit = sqrt(120**2 - self.fixed_position**2)

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

    def set_fixed_position(self, value):
        """Set our `fixed_position`."""
        self.fixed_position = value
        self.x = self.calculate_start_x()
        self.final_x = 0 - self.x

    def randomise_offset(self):
        """Set fixed_position to something random."""
        self.set_fixed_position(
            randint(int(-self.fixed_position_limit), int(self.fixed_position_limit))
        )

    def move(self):
        """Walk."""
        increment = self.speed * self.scale * self.conf["movement-factors"][self.name]
        if self.flipped:
            self.x -= increment
        else:
            self.x += increment
        self.y = self.fixed_position
