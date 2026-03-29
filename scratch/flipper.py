import json
from pathlib import Path

data = json.loads(Path("bitmaps/pickaxe/regular.json").read_text())

flipped = []
for sprite in data:
    flipped.append([])
    for row in sprite:
        flipped[-1].append(list(reversed(row)))

Path("bitmaps/pickaxe/inverted.json").write_text(json.dumps(flipped))
