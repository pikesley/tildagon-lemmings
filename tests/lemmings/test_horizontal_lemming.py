from lib.lemmings.horizontal_lemming import HorizontalLemming
from tests.helpers import test_defaults


def test_y_limit():
    """Test."""
    h_lem = HorizontalLemming("square", test_defaults)

    assert h_lem.y_limit == 116


def test_start_position():
    """Test."""
    h_lem = HorizontalLemming("square", test_defaults)

    assert h_lem.x == -128


def test_end_position():
    """Test."""
    params = dict(test_defaults)
    params["flipped"] = True
    h_lem = HorizontalLemming("square", params)

    assert h_lem.x == 128
    assert h_lem.final_x == -128


def test_start_position_when_offset():
    """Test."""
    h_lem = HorizontalLemming("square", test_defaults)
    h_lem.set_y(-60)

    assert h_lem.x == -112
