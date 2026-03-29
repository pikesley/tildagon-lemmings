from ..lemming import Lemming


class HorizontalLemming(Lemming):
    """A walking lemming."""

    def __init__(self, params):
        """Construct."""
        super().__init__(params)

        self.scaling_dimension = self.width
        self.configure()

    def update_x_y(self):
        """Update `x` and `y` (mostly for `draw()` purposes)."""
        self.y = self.fixed_position
        self.x = self.variable_position

    def move(self):
        """Walk."""
        increment = self.speed * self.scale * self.conf["movement-factors"][self.name]
        if self.flipped:
            self.variable_position -= increment
        else:
            self.variable_position += increment

        self.update_x_y()

    def set_fixed_position(self, value):
        """Set our `fixed_position`."""
        super().set_fixed_position(value)
        self.x = self.variable_position

    def calculate_start_variable_position(self):
        """Starting `variable_position`."""
        position = super().calculate_start_variable_position()
        if self.flipped:
            position = -position

        return position
