from pathlib import Path

files = Path("bitmaps/basher-1/").glob("*")

for file in files:
    print(file)
