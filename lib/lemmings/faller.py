from .vertical_lemming import VerticalLemming


class Faller(VerticalLemming):
    """A faller."""

    def __init__(self, params=None):
        """Construct."""
        super().__init__("faller", params or {})

    def move(self):
        """Walk."""
        self.y += self.speed * self.scale
