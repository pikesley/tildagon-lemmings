from .horizontal_lemming import HorizontalLemming


class Walker(HorizontalLemming):
    """A walker."""

    def __init__(self, params=None):
        """Construct."""
        super().__init__("walker", params or {})

    def move(self):
        """Walk."""
        if self.flipped:
            self.x -= self.speed * self.scale
        else:
            self.x += self.speed * self.scale
