import json
from pathlib import Path

lookups = {
    "[0, 0, 0]": "bg",
    "[95, 99, 255]": "cl",
    "[0, 179, 0]": "hr",
    "[255, 235, 223]": "sk",
    "[255, 255, 0]": "um",
    "[99, 0, 19]": "dt",
    "[255, 0, 0]": "sc",
}

data = json.loads(Path("bitmaps/bridger.json").read_text())

colours = set()

colourised = []
for sprite in data:
    colourised.append([])
    for row in sprite:
        for x in row:
            colours.add(str(x))
        fixed = [lookups[str(x)] for x in row]
        colourised[-1].append(fixed)

print(colours)

Path("bitmaps", "bridger-colours.json").write_text(
    json.dumps(colourised), encoding="utf-8"
)
