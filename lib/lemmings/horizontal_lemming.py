from ..lemming import Lemming


class HorizontalLemming(Lemming):
    """A walking lemming."""

    def __init__(self, params):
        """Construct."""
        super().__init__(params)

        self.x = self.variable_position
        self.y = self.fixed_position

    def move(self):
        """Walk."""
        increment = self.speed * self.scale * self.conf["movement-factors"][self.name]
        if self.flipped:
            self.variable_position -= increment
        else:
            self.variable_position += increment

        self.x = self.variable_position
        self.y = self.fixed_position

    def set_fixed_position(self, value):
        """Set our `fixed_position`."""
        super().set_fixed_position(value)
        self.x = self.variable_position
