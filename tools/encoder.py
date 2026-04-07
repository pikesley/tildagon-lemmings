import gzip
import json
from pathlib import Path

import yaml

conf = yaml.safe_load(Path("conf.yaml").read_text(encoding="utf-8"))
background_symbol = "bg"


def encode_line(line):
    """Encode just the `on` elements from a line."""
    result = []

    current = line[0]
    count = 0
    start_index = 0

    for index, char in enumerate(line):
        if char == current:
            count += 1
        else:
            if current != background_symbol:
                result.append([current, start_index, count])
            current = char
            count = 1
            start_index = index

    if current != background_symbol:
        result.append([current, start_index, count])

    return result


def scale_encode_line(line, scale):
    """Encode with scale and offset."""
    return [[(e[0] - len(line) / 2) * scale, e[1] * scale] for e in encode_line(line)]


def encode_block(block):
    """Encode a block of text."""
    result = []

    for index, line in enumerate(block):
        result.extend([x + [index] for x in encode_line(line)])

    return result


def scale_encode_block(block, scale):
    """Scale-encode a block of text."""
    scaled_lines = [scale_encode_line(line, scale=scale) for line in block.split("\n")]
    result = []
    offset = len(scaled_lines) / 2

    for index, line in enumerate(scaled_lines):
        result.extend([item + [(index - offset) * scale] for item in line])

    return result


def encode(block):
    """Encode."""
    return encode_block(block)


if __name__ == "__main__":
    from pathlib import Path

    outdir = Path(
        "sources/encoded",
    )
    outdir.mkdir(exist_ok=True, parents=True)

    for move in Path("sources/slimmed_bitmaps").glob("*"):
        print(move)

        movedir = Path(outdir, move.stem)
        movedir.mkdir(exist_ok=True, parents=True)

        encodeds = {"regular": [], "inverted": []}

        for file in sorted(Path(move).glob("*")):
            data = json.loads(file.read_text(encoding="utf-8"))
            encodeds["regular"].append(encode(data))
            encodeds["inverted"].append(encode([list(reversed(x)) for x in data]))

        for key, data in encodeds.items():
            Path(movedir, f"{key}.json.gz").write_bytes(
                gzip.compress(json.dumps(data).encode("utf-8"), mtime=None)
            )
