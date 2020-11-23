import os
from ast import literal_eval
from utils import find_coeffs
from PIL import Image, ImageOps

template = 'lick'
img = Image.open('input.png')

bg = Image.open(f'templates/{template}/bg.png')
masks = [Image.open(f'templates/{template}/{m}') for m in filter(lambda x: x.startswith('mask'), os.listdir(f'templates/{template}'))]

img = img.resize(bg.size)

with open(f'templates/{template}/matrix.txt') as f:
    matrixs = literal_eval(f.read())


for matrix, mask in zip(matrixs, masks):
    coeffs = find_coeffs([(0, 0), (bg.size[0], 0), (bg.size[0], bg.size[1]), (0, bg.size[1])], matrix)
    t = img.transform(bg.size, Image.PERSPECTIVE, coeffs, Image.BICUBIC)
    bg.paste(t, (0, 0), mask)

# bg = ImageOps.autocontrast(bg, cutoff=3)
bg.show()
