from ..vertical_lemming import VerticalLemming


class Umbrella(VerticalLemming):
    """An umbrella faller."""

    def __init__(self, params=None):
        """Construct."""
        self.name = "umbrella"
        super().__init__(params or {})
