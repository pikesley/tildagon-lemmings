from lib.lemmings.walker import Walker
from tests.helpers import test_defaults


def test_walker():
    """Test."""
    w = Walker(test_defaults)
    assert w.variety == "walker"


def test_positioning():
    """Test."""
    w = Walker(test_defaults)
    w.x = 0
    assert w.pixels[0].centre[0] == (-20)


def test_larger_positioning():
    """Test."""
    w = Walker(
        {
            "scale": 16,
            "asset-path": "tests/fixtures/",
        }
    )
    w.x = 0
    assert w.pixels[0].centre[0] == (-80)
