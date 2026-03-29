from lib.lemmings.vertical_lemmings.digger import Digger
from tests.helpers import test_defaults

params = dict(test_defaults, name="digger")


def test_digger():
    """Test."""
    d = Digger(params)
    assert d.name == "digger"


def test_start_position():
    """Test."""
    d = Digger(params)

    assert d.x == 0
    assert d.y == d.variable_position == -172
    assert d.final_variable_position == 172
