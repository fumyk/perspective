from ast import literal_eval
from utils import find_coeffs
from PIL import Image, ImageOps

template = '2b'
img = Image.open('input.png')

bg = Image.open(f'templates/{template}/bg.png')
mask = Image.open(f'templates/{template}/mask.png')
# preview = Image.open(f'templates/{template}/preview.png')

img = img.resize(bg.size)

with open(f'templates/{template}/matrix.txt') as f:
    matrix = literal_eval(f.read())

coeffs = find_coeffs([(0, 0), (bg.size[0], 0), (bg.size[0], bg.size[1]), (0, bg.size[1])], matrix)

img = img.transform(bg.size, Image.PERSPECTIVE, coeffs, Image.BICUBIC)

bg.paste(img, (0, 0), mask)
# bg = ImageOps.autocontrast(bg, cutoff=3)
bg.show()
