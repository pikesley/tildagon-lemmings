from math import sqrt
from random import randint

from ..lemming import Lemming


class VerticalLemming(Lemming):
    """An up-down lemming."""

    def __init__(self, params):
        """Construct."""
        super().__init__(params)

        self.scaling_dimension = self.width
        self.fixed_position = 0
        self.fixed_position_limit = 120 - ((self.scaling_dimension / 2) * self.scale)

        if self.params["randomised-offset"]:
            self.randomise_offset()

        self.variable_position = self.calculate_start_variable_position()
        self.final_variable_position = 0 - self.variable_position

        self.x = self.fixed_position
        self.y = self.variable_position

    def calculate_start_variable_position(self):
        """Starting x-position."""
        limit = sqrt(120**2 - self.fixed_position**2)

        position = -limit - (self.width * self.scale)
        if self.flipped:
            position = limit + (self.width * self.scale)

        return round(position)

    @property
    def done(self):
        """Are we off-screen?"""
        return self.variable_position > self.final_variable_position

    def set_fixed_position(self, value):
        """Set our `fixed_position`."""
        self.fixed_position = value
        self.variable_position = self.calculate_start_variable_position()
        self.final_variable_position = 0 - self.variable_position

    def randomise_offset(self):
        """Set fixed_position to something random."""
        self.set_fixed_position(
            randint(int(-self.fixed_position_limit), int(self.fixed_position_limit))
        )

    def move(self):
        """Dig."""
        increment = self.speed * self.scale * self.conf["movement-factors"][self.name]
        self.variable_position += increment

        self.x = self.fixed_position
        self.y = self.variable_position
