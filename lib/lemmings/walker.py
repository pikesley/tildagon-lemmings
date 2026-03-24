from .horizontal_lemming import HorizontalLemming


class Walker(HorizontalLemming):
    """A walker."""

    def __init__(self, offset=0, scale=4, speed=1, flipped=False):
        """Construct."""
        super().__init__(
            variety="walker",
            y=offset,
            scale=scale,
            speed=speed,
            flipped=flipped,
        )

    def move(self):
        """Walk."""
        if self.flipped:
            self.x -= self.speed * self.scale
        else:
            self.x += self.speed * self.scale
