from .horizontal_lemming import HorizontalLemming


class Walker(HorizontalLemming):
    """A walker."""

    def __init__(self, params=None):
        """Construct."""
        self.name = "walker"
        super().__init__(params or {})
