from lib.lemmings.horizontal_lemming import HorizontalLemming
from tests.helpers import test_defaults


def test_y_limit():
    """Test."""
    h_lem = HorizontalLemming("square", test_defaults)

    assert h_lem.y_limit == 116


def test_start_position():
    """Test."""
    h_lem = HorizontalLemming("square", test_defaults)

    assert h_lem.start_x == -128
