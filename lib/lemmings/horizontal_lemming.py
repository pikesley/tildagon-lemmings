from ..lemming import Lemming


class HorizontalLemming(Lemming):
    """A walking lemming."""

    def __init__(  # noqa: PLR0913
        self,
        variety,
        y=0,
        scale=4,
        speed=1,
        flipped=False,
        asset_path=None,
        compressed_bitmaps=True,
    ):
        """Construct."""
        super().__init__(
            variety=variety,
            scale=scale,
            speed=speed,
            flipped=flipped,
            asset_path=asset_path,
            compressed_bitmaps=compressed_bitmaps,
        )

        self.y_limit = 120 - (((self.height / 2) * self.scale) + (self.scale / 2))

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
