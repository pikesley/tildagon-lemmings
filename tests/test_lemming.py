from helpers import test_defaults

from lib.lemming import Lemming


def test_lemming():
    """Test."""
    lem = Lemming(test_defaults)
    lem.name = "square"
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
    lem = Lemming(test_defaults)
    lem.name = "square"
    lem.x = 0
    lem.y = 0

    assert lem.pixels[0].top == -4
    assert lem.pixels[0].left == -4
