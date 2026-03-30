class Background:
    """Background."""

    def __init__(self, bottom_colour=(255, 0, 255), top_colour=(0, 0, 0)):
        """Construct."""
        self.bottom_colour = bottom_colour
        self.top_colour = top_colour

    def draw(self, ctx):
        """Draw ourself."""
        ctx.linear_gradient(0, -120, 0, 120)

        ctx.add_stop(0.0, self.top_colour, 1.0)
        ctx.add_stop(1.0, self.bottom_colour, 1.0)

        ctx.rectangle(-120, -120, 240, 240).fill()
