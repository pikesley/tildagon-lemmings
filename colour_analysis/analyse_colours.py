from pathlib import Path
import json
import gzip

rgbs = []
for sprite in Path("bitmaps").glob("**/*"):
    if sprite.is_file():
        data = json.loads(gzip.decompress(sprite.read_bytes()))
        for row in data:
            for rgb in row:
                expanded = [int(x * 255) for x in rgb[0:3]]
                if expanded not in rgbs:
                    rgbs.append(expanded)

s = ":root {\n"
for index, rgb in enumerate(rgbs):
    s += f"  --rgb-{index}: rgb({rgb[0]}, {rgb[1]}, {rgb[2]});\n"
s += "}"

Path("colour_analysis/scratch.css").write_text(s, encoding="utf-8")
