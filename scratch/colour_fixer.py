import colorsys

colours = {
    "background": [1, 0, 1],
    "hair": [0.0, 0.7019607843137254, 0.0],
    "flesh": [1.0, 0.9215686274509803, 0.8745098039215686],
    "clothing": [0.37254901960784315, 0.38823529411764707, 1.0],
}

hsv_colours = {}

for key, rgb in colours.items():
    hsv = colorsys.rgb_to_hsv(*[x * 255 for x in rgb])
    hsv_colours[key] = {"hue": hsv[0], "value": hsv[2]}

print(hsv_colours)
