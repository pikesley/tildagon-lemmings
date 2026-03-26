class Pixel:
    """A square."""

    def __init__(self, top_left, size, colour, opacity):
        """Construct."""
        self.top, self.left = top_left
        self.size = size
        self.colour = list(colour) + [opacity]

    def draw(self, ctx):
        """Draw."""
        ctx.translate(self.top, self.left)
        ctx.rgba(*self.colour)

        ctx.rectangle(self.top, self.left, self.top + self.size, self.left + self.size)

        ctx.fill()
