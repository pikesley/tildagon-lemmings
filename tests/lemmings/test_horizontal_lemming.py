from lib.lemmings.horizontal_lemming import HorizontalLemming
from tests.helpers import test_defaults


def test_fixed_position_limit():
    """Test."""
    h_lem = HorizontalLemming(test_defaults)

    assert h_lem.fixed_position_limit == 116


def test_start_position():
    """Test."""
    h_lem = HorizontalLemming(test_defaults)

    assert h_lem.x == -128


def test_end_position():
    """Test."""
    params = dict(test_defaults)
    params["flipped"] = True
    h_lem = HorizontalLemming(params)

    assert h_lem.x == 128
    assert h_lem.final_variable_position == -128


def test_start_position_when_offset():
    """Test."""
    h_lem = HorizontalLemming(test_defaults)
    h_lem.set_fixed_position(-60)

    assert h_lem.x == -112


def test_moonwalker():
    """Test."""
    params = dict(test_defaults)
    l_r_lem = HorizontalLemming(params)
    assert l_r_lem.x == -128
    assert l_r_lem.pixels[0].colour[-1] == 1
    assert l_r_lem.pixels[1].colour[-1] == 0

    params = dict(test_defaults, flipped=True)
    r_l_lem = HorizontalLemming(params)
    assert r_l_lem.x == 128
    assert r_l_lem.pixels[0].colour[-1] == 0
    assert r_l_lem.pixels[1].colour[-1] == 1

    params = dict(test_defaults, moonwalker=True)
    l_r_moonwalker = HorizontalLemming(params)
    assert l_r_moonwalker.x == -128
    assert l_r_moonwalker.pixels[0].colour[-1] == 0
    assert l_r_moonwalker.pixels[1].colour[-1] == 1

    params = dict(test_defaults, flipped=True, moonwalker=True)
    r_l_moonwalker = HorizontalLemming(params)
    assert r_l_moonwalker.x == 128
    assert r_l_moonwalker.pixels[0].colour[-1] == 1
    assert r_l_moonwalker.pixels[1].colour[-1] == 0
