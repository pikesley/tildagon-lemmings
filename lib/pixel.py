class Pixel:
    """A rectangle."""

    def __init__(self, left, width, top, height, colour):
        """Construct."""
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.colour = colour

    def draw(self, ctx):
        """Draw."""
        ctx.rgba(*self.colour)

        ctx.rectangle(
            self.left,
            self.top,
            self.width,
            self.height,
        )

        ctx.fill()
