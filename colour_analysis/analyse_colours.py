import json
from pathlib import Path

rgbs = []

data = json.loads(Path("bitmaps", "walker.json").read_text(encoding="utf-8"))
for sprite in data:
    for row in sprite:
        for rgb in row:
            expanded = [int(x * 255) for x in rgb[0:3]]
            if expanded not in rgbs:
                rgbs.append(expanded)

s = ":root {\n"
for index, rgb in enumerate(rgbs):
    s += f"  --rgb-{index}: rgb({rgb[0]}, {rgb[1]}, {rgb[2]});\n"
s += "}"

Path("colour_analysis/scratch.css").write_text(s, encoding="utf-8")
