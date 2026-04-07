from pathlib import Path

from PIL import Image

for lemming in Path("sources/strips").glob("*"):
    print(lemming)
    outdir = Path("sources/crops", lemming.stem)
    outdir.mkdir(exist_ok=True, parents=True)

    strip = Image.open(lemming)
    for i in range(int(strip.width / 16)):
        left = i * 16
        right = left + 16
        height = strip.height
        filename = f"{str(i).zfill(2)}.png"

        with Path.open(f"{outdir}/{filename}", "wb") as f:
            strip.crop((left, 0, right, height)).save(f)
