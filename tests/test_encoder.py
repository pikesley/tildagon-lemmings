from tools.encoder import (
    encode_block,
    encode_line,
)


def test_line_encode():
    """Test."""
    assert encode_line(["bg", "bg", "hr", "hr", "bg", "bg"]) == [["hr", 2, 2]]
    assert encode_line(
        [
            "hr",
            "hr",
            "bg",
            "bg",
            "sk",
            "sk",
        ]
    ) == [["hr", 0, 2], ["sk", 4, 2]]


def test_block_encode():
    """Test."""
    fixture = [["bg", "bg", "hr", "hr", "bg", "bg"]]
    assert encode_block(fixture) == [["hr", 2, 2, 0]]

    fixture = """111000111
000111111
101110010"""
    fixture = [
        ["bg", "bg", "hr", "hr", "bg", "bg"],
        ["hr", "hr", "bg", "bg", "hr", "hr"],
        ["bg", "bg", "hr", "hr", "bg", "bg"],
    ]
    assert encode_block(fixture) == [
        ["hr", 2, 2, 0],
        ["hr", 0, 2, 1],
        ["hr", 4, 2, 1],
        ["hr", 2, 2, 2],
    ]
