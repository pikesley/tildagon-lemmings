from .vertical_lemming import VerticalLemming


class Umbrella(VerticalLemming):
    """An umbrella faller."""

    def __init__(self, params=None):
        """Construct."""
        super().__init__("umbrella", params or {})

    def move(self):
        """Fall."""
        self.y += self.speed * 0.5 * self.scale
