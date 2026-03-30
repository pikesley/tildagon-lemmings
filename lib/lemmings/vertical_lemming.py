from ..lemming import Lemming


class VerticalLemming(Lemming):
    """An up-down lemming."""

    def __init__(self, params):
        """Construct."""
        super().__init__(params)

        self.scaling_dimension = self.height
        self.configure()

    def update_x_y(self):
        """Update `x` and `y` (mostly for `draw()` purposes)."""
        self.x = self.fixed_position
        self.y = self.variable_position

    def move(self):
        """Move."""
        self.variable_position += (
            self.movement_increment * self.steps_per_frame[self.frame_index]
        )
        self.update_x_y()

    def set_fixed_position(self, value):
        """Set our `fixed_position` (`x`)."""
        super().set_fixed_position(value)
        self.y = self.variable_position
