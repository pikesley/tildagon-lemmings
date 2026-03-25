import gzip
import json
import sys
from itertools import batched
from pathlib import Path

from PIL import Image

img = Image.open(sys.argv[1])
lemming = sys.argv[1].split("/")[-1].split(".")[0]

root_path = Path("bitmaps", lemming)
root_path.mkdir(exist_ok=True)

compress = False
if len(sys.argv) > 2:
    compress = True

sprite_count = int(img.width / 16)
sprites = {}
for i in range(sprite_count):
    sprites[i] = []


for index, row in enumerate(batched(img.get_flattened_data(), 16)):
    fixed_row = []
    for item in row:
        if item[0:3] == (0, 0, 0):
            item = (0, 0, 0, 0)  # noqa: PLW2901
        fixed_row.append([x / 255 for x in item])

    sprites[index % sprite_count].append(fixed_row)

for key, pixels in sprites.items():
    if compress:
        Path(root_path, f"{key}.json.gz").write_bytes(
            gzip.compress(json.dumps(pixels).encode("utf-8"))
        )
    else:
        Path(root_path, f"{key}.json").write_text(
            json.dumps(pixels, indent=2), encoding="utf-8"
        )
