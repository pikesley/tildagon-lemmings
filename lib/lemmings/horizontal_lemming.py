from ..lemming import Lemming


class HorizontalLemming(Lemming):
    """A walking lemming."""

    def __init__(self, variety, y=0, scale=4, speed=1, flipped=False):
        """Construct."""
        super().__init__(
            variety=variety,
            scale=scale,
            speed=speed,
            flipped=flipped,
        )

        self.x = -120 - (len(self.frames[0]) * self.scale)
        if self.flipped:
            self.x = 120 + (len(self.frames[0]) * self.scale)

        self.y = y

    @property
    def done(self):
        """Are we off-screen?"""
        if self.flipped:
            return self.x < -120 - (len(self.frames[0]) * self.scale)
        return self.x > 120
