from ..horizontal_lemming import HorizontalLemming


class Pickaxe(HorizontalLemming):
    """A pickaxe-digger."""

    def __init__(self, params=None):
        """Construct."""
        self.name = "pickaxe"
        super().__init__(params or {})

    def move(self):
        """Walk."""
        increment = (
            self.speed
            * self.scale
            * self.conf["movement-controls"][self.name]["scale-factor"]
        )
        if self.frame_index in [3, 15]:
            if self.flipped:
                self.variable_position -= increment
            else:
                self.variable_position += increment

        self.update_x_y()
