from helpers import test_defaults

from lib.lemming import Lemming


def test_lemming():
    """Test."""
    lem = Lemming("square", test_defaults)
    assert lem.frames == [
        [
            ["hair", "background"],
            ["hair", "background"],
        ],
        [
            ["hair", "background"],
            ["hair", "background"],
        ],
    ]


def test_positioning():
    """Test."""
    lem = Lemming("square", test_defaults)

    lem.x = 0
    lem.y = 0

    assert lem.pixels[0].centre == (-4, -4)
