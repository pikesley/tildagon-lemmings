from ..horizontal_lemming import HorizontalLemming


class Pickaxe(HorizontalLemming):
    """A pickaxe-digger."""

    def __init__(self, params=None):
        """Construct."""
        self.name = "pickaxe"
        super().__init__(params or {})

    # def move(self):
    #     """Walk."""
    #     if self.frame_index in [3, 15]:
    #         if self.flipped:
    #             self.variable_position -= self.movement_increment
    #         else:
    #             self.variable_position += self.movement_increment

    #     self.update_x_y()
