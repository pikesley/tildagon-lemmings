from ..lemming import Lemming


class VerticalLemming(Lemming):
    """An up-down lemming."""

    def __init__(self, variety, x=0, scale=4, speed=1, flipped=False):
        """Construct."""
        super().__init__(
            variety=variety,
            scale=scale,
            speed=speed,
            flipped=flipped,
        )

        self.y = -120 - (len(self.frames[0]) * self.scale)
        if self.flipped:
            self.y = 120 + (len(self.frames[0]) * self.scale)

        self.x = x

    @property
    def done(self):
        """Are we off-screen?"""
        return self.y > 120 + (len(self.frames[0]) * self.scale)
