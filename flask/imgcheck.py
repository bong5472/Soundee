import extcolors
from PIL import Image

def imgchecking(imgsrc):
    rgb_arr = []
    rgb_percent = []
    img = Image.open(imgsrc)
    colors, pixel_count = extcolors.extract_from_image(img)

    pixel_output = 0
    for c in colors:
        pixel_output += c[1]
        rgb_arr.append(list(c[0]))
        rgb_percent.append(round((c[1] / pixel_count) * 100, 2))
        # print(f'{c[0]} : {round((c[1] / pixel_count) * 100, 2)}% ({c[1]})')
    # print(rgb_arr)
    return rgb_arr[0], rgb_arr[1]

