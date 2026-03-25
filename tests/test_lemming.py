from lib.lemming import Lemming


def test_lemming():
    """Test."""
    lem = Lemming(
        "square", scale=4, asset_path="tests/fixtures/", compressed_bitmaps=False
    )
    assert lem.frames == [
        [
            [[1.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 1.0]],
            [[1.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 1.0]],
        ]
    ]


def test_positioning():
    """Test."""
    lem = Lemming(
        "square", scale=4, asset_path="tests/fixtures/", compressed_bitmaps=False
    )

    lem.x = 0
    lem.y = 0

    assert lem.pixels[0].centre == (-2, -2)
