import json
from pathlib import Path

frames = {}

leading = 16
trailing = 16

for j in Path("bitmaps/walker").glob("*"):
    frames[int(j.stem)] = json.loads(j.read_text(encoding="utf-8"))


for data in frames.values():
    for row in data:
        l_counter = 0
        for pixel in row:
            if pixel != [0, 0, 0]:
                if l_counter < leading:
                    leading = l_counter
                    break
            else:
                l_counter += 1

        r_counter = 0
        for pixel in reversed(row):
            if pixel != [0, 0, 0]:
                if r_counter < trailing:
                    trailing = r_counter
                    break
            else:
                r_counter += 1

slimmed = []
for key in sorted(frames.keys()):
    slimmed.append([])
    for row in frames[key]:
        slimmed[-1].append(row[leading:-trailing])

Path("bitmaps/walker.json").write_text(json.dumps(slimmed))
