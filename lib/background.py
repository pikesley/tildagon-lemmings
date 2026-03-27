from .asset_path import ASSET_PATH


class Background:
    """Background."""

    def __init__(
        self,
        colour=(0, 0, 0),
        opacity=1,
    ):
        """Construct."""
        self.colour = list(colour) + [opacity]

    def draw(self, ctx):
        """Draw ourself."""
        # ctx.image(ASSET_PATH + "images/emf.png", -120, -120, 240, 240)
        ctx.rgba(*self.colour).rectangle(-120, -120, 240, 240).fill()
