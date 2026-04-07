import json
from pathlib import Path

margins = {}

for move in Path("sources/bitmaps").glob("*"):
    print(move)
    leading = 16
    trailing = 16

    for j in Path(move).glob("*"):
        data = json.loads(j.read_text(encoding="utf-8"))

        for row in data:
            l_counter = 0
            for pixel in row:
                if pixel != "bg":
                    if l_counter < leading:
                        leading = l_counter
                        break
                else:
                    l_counter += 1

            r_counter = 0
            for pixel in reversed(row):
                if pixel != "bg":
                    if r_counter < trailing:
                        trailing = r_counter
                        break
                else:
                    r_counter += 1

        margins[move.stem] = {"leading": leading, "trailing": trailing}

for move in Path("sources/bitmaps").glob("*"):
    print(move)
    frames = []
    outdir = Path("sources/slimmed_bitmaps", move.name)
    outdir.mkdir(exist_ok=True, parents=True)
    for j in Path(move).glob("*"):
        data = json.loads(j.read_text(encoding="utf-8"))

        slimmed = []
        ends = tuple(margins[move.stem].values())
        for row in data:
            if ends in ((0, 0), (1, 0)):
                slimmed.append(row[:])
            else:
                slimmed.append(row[ends[0] : -ends[1]])

        frames.append(slimmed[:])
        Path(outdir, f"{j.name}").write_text(
            json.dumps(slimmed, indent=2), encoding="utf-8"
        )
