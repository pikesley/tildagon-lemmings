from ..horizontal_lemming import HorizontalLemming


class Basher(HorizontalLemming):
    """A basher."""

    def __init__(self, params=None):
        """Construct."""
        self.name = "basher"
        super().__init__(params or {})
