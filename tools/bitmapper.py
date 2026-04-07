import json
from itertools import batched
from pathlib import Path

from PIL import Image

lookups = {
    "[0, 0, 0]": "bg",
    "[95, 99, 255]": "cl",
    "[0, 179, 0]": "hr",
    "[0, 180, 0]": "hr",
    "[255, 235, 223]": "sk",
    "[255, 236, 224]": "sk",
    "[255, 255, 0]": "um",
    "[99, 0, 19]": "dt",
    "[99, 0, 11]": "dt",
    "[255, 0, 0]": "sc",
}

for move in Path("sources/crops").glob("*"):
    print(move)
    outdir = Path("sources/bitmaps", move.name)
    outdir.mkdir(exist_ok=True, parents=True)
    for file in Path(move).glob("*"):
        img = Image.open(file)
        data = [
            [lookups[str(list(x[0:3]))] for x in row]
            for row in batched(img.get_flattened_data(), img.width)
        ]

        Path(outdir, f"{file.stem}.json").write_text(
            json.dumps(data, indent=2), encoding="utf-8"
        )
