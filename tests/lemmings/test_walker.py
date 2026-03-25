from lib.lemmings.walker import Walker
from tests.helpers import test_defaults


def test_walker():
    """Test."""
    params = dict(test_defaults)
    params["compressed-bitmaps"] = True
    w = Walker(params)
    assert w.variety == "walker"
