from .vertical_lemming import VerticalLemming


class Digger(VerticalLemming):
    """A digger."""

    def __init__(self, params=None):
        """Construct."""
        self.name = "digger"
        super().__init__(self.name, params or {})
