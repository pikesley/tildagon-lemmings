class Pixel:
    """A square."""

    def __init__(self, left, top, size, colour, opacity, dot=False):  # noqa: PLR0913
        """Construct."""
        self.left = left
        self.top = top
        self.size = size
        self.colour = list(colour) + [opacity]
        self.dot = dot

    def draw(self, ctx):
        """Draw."""
        ctx.rgba(*self.colour)

        if self.dot:
            ctx.round_rectangle(
                self.left + 1,
                self.top + 1,
                self.size - 1,
                self.size - 1,
                self.size - 2,
            )

        else:
            ctx.rectangle(
                self.left,
                self.top,
                self.size,
                self.size,
            )

        ctx.fill()
