from ..lemming import Lemming


class Basher(Lemming):
    """A walker."""

    def __init__(self, y=-80, scale=5, speed=1, flipped=False):
        """Construct."""
        super().__init__(
            variety="basher",
            y=y,
            scale=scale,
            speed=speed,
            flipped=flipped,
        )

    def move(self):
        """Bash."""
        moduli = [11, 12, 13, 14]
        for modulus in moduli:
            if self.frame_index % modulus == 0:
                if self.flipped:
                    self.x -= self.speed * self.scale
                else:
                    self.x += self.speed * self.scale
