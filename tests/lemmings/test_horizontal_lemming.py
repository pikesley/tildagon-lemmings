from lib.lemmings.horizontal_lemming import HorizontalLemming


def test_y_limit():
    """Test."""
    h_lem = HorizontalLemming(
        "square",
        scale=4,
        asset_path="tests/fixtures/",
        compressed_bitmaps=False,
    )

    assert h_lem.y_limit == 116
