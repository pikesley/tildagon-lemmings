from helpers import test_defaults

from lib.lemming import Lemming


def test_lemming():
    """Test."""
    lem = Lemming("square", test_defaults)
    assert lem.frames == [
        [
            ["hr", "bg"],
            ["hr", "bg"],
        ],
        [
            ["hr", "bg"],
            ["hr", "bg"],
        ],
    ]


def test_positioning():
    """Test."""
    lem = Lemming("square", test_defaults)

    lem.x = 0
    lem.y = 0

    assert lem.pixels[0].top == -4
    assert lem.pixels[0].left == -4
