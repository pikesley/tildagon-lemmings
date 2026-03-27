from lib.colony import Colony


def test_colony():
    """Test."""
    test_conf = {
        "lemming-count": 3,
        "scale": {"min": 1, "max": 3},
        "moonwalk-threshold": 1,
        "faller-threshold": 1,
    }

    col = Colony(1.0, test_conf)

    assert len(col.lemmings) == 3
    assert sorted([lemming.scale for lemming in col.lemmings]) == [1, 2, 3]
