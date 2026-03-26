from pathlib import Path

import yaml

colours = {
    "magenta": [221, 0, 255],
    "yellow": [246, 255, 0],
    "red": [255, 0, 0],
    "cream": [255, 235, 223],
    "grey": [164, 164, 164],
    "green": [0, 179, 0],
    "white": [255, 255, 255],
    "orange": [250, 175, 0],
    "blue": [0, 170, 255],
    "indigo": [95, 99, 255],
}

fixed = {}
for key, rgb in colours.items():
    fixed[key] = [x / 255 for x in rgb]

Path("foo.yaml").write_text(yaml.dump(fixed))
