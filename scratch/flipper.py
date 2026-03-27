import json
from pathlib import Path

data = json.loads(Path("bitmaps/umbrella.json").read_text())

flipped = []
for sprite in data:
    flipped.append([])
    for row in sprite:
        flipped[-1].append(list(reversed(row)))

Path("bitmaps/umbrella-flipped.json").write_text(json.dumps(flipped))
