from math import sqrt

from ..lemming import Lemming


class VerticalLemming(Lemming):
    """An up-down lemming."""

    def __init__(self, params):
        """Construct."""
        super().__init__(params)

        self.x = self.fixed_position
        self.y = self.variable_position

    def calculate_start_variable_position(self):
        """Starting x-position."""
        limit = sqrt(120**2 - self.fixed_position**2)

        position = -limit - (self.width * self.scale)
        if self.flipped:
            position = limit + (self.width * self.scale)

        return round(position)

    def move(self):
        """Dig."""
        increment = self.speed * self.scale * self.conf["movement-factors"][self.name]
        self.variable_position += increment

        self.x = self.fixed_position
        self.y = self.variable_position
