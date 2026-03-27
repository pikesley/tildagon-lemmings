import json
from pathlib import Path

lookups = {
    "[0, 0, 0]": "bg",
    "[0, 179, 0]": "hr",
    "[255, 235, 223]": "sk",
    "[95, 99, 255]": "cl",
}

data = json.loads(Path("bitmaps/faller.json").read_text())

colourised = []
for sprite in data:
    colourised.append([])
    for row in sprite:
        fixed = [lookups[str(x)] for x in row]
        colourised[-1].append(fixed)

Path("bitmaps", "faller-colours.json").write_text(
    json.dumps(colourised), encoding="utf-8"
)
