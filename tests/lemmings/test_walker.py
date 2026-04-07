from lib.lemmings.horizontal_lemmings.walker import Walker
from tests.helpers import test_defaults

params = dict(test_defaults, name="walker")


def test_walker():
    """Test."""
    w = Walker(params)
    assert w.name == "walker"


def test_positioning():
    """Test."""
    w = Walker(params)
    w.x = 0
    assert w.pixels[0].left == -8


def test_larger_positioning():
    """Test."""
    w = Walker({"scale": 16, "asset-path": "tests/fixtures/", "name": "walker"})
    w.x = 0
    assert w.pixels[0].top == -64
    assert w.pixels[0].left == -32
