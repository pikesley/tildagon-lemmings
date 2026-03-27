from lib.colony import Colony


def test_scale_exclusion():
    """Test all sizes are different."""
    test_conf = {
        "lemming-count": 3,
        "scale": {"min": 1, "max": 3},
        "thresholds": {
            "freak": 1,
            "moonwalk": 1,
        },
    }
    col = Colony(1.0, test_conf)

    assert len(col.lemmings) == 3
    assert sorted([lemming.scale for lemming in col.lemmings]) == [1, 2, 3]


def test_freak_exclusion():
    """Test at-most 1 freak."""
    test_conf = {
        "lemming-count": 3,
        "scale": {"min": 1, "max": 3},
        "thresholds": {
            "freak": 0,
            "moonwalk": 1,
        },
    }
    col = Colony(1.0, test_conf)

    assert len(col.lemmings) == 3
    assert (
        len(list(filter(lambda x: x.__class__.__name__ != "Walker", col.lemmings))) == 1
    )
    assert col.freak_token == 0


def test_correct_colouring():
    """Test only moonwalkers have inverse colours."""
