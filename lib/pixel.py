class Pixel:
    """A square."""

    def __init__(self, left, top, size, colour, opacity):
        """Construct."""
        self.left = left
        self.top = top
        self.size = size
        self.colour = list(colour) + [opacity]

    def draw(self, ctx):
        """Draw."""
        ctx.rgba(*self.colour)

        ctx.rectangle(
            self.left,
            self.top,
            self.size,
            self.size,
        )

        ctx.fill()
