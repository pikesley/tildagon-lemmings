from ..horizontal_lemming import HorizontalLemming


class Bridger(HorizontalLemming):
    """A bridger."""

    def __init__(self, params=None):
        """Construct."""
        self.name = "bridger"
        super().__init__(params or {})
