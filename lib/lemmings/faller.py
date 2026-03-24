from .vertical_lemming import VerticalLemming


class Faller(VerticalLemming):
    """A walker."""

    def __init__(self, offset=0, scale=4, speed=1, flipped=False):
        """Construct."""
        super().__init__(
            variety="faller",
            x=offset,
            scale=scale,
            speed=speed,
            flipped=flipped,
        )

    def move(self):
        """Fall."""
        self.y += self.speed * self.scale
