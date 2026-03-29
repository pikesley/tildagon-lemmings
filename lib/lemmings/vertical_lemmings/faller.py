from ..vertical_lemming import VerticalLemming


class Faller(VerticalLemming):
    """A faller."""

    def __init__(self, params=None):
        """Construct."""
        self.name = "faller"
        super().__init__(params or {})
