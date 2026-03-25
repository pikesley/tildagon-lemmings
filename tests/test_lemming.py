from helpers import test_defaults

from lib.lemming import Lemming


def test_lemming():
    """Test."""
    lem = Lemming("square", test_defaults)
    assert lem.frames == [
        [
            [[1.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 1.0]],
            [[1.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 1.0]],
        ]
    ]


def test_positioning():
    """Test."""
    lem = Lemming("square", test_defaults)

    lem.x = 0
    lem.y = 0

    assert lem.pixels[0].centre == (-2, -2)
