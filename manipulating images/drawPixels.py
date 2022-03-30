# Changing individual pixels

from PIL import Image
from PIL import ImageColor

# new image square 100x100
im = Image.new('RGBA', (100, 100))
px = im.getpixel((0, 0))

print(f'pixel 0,0 : {px}')

# paint light grey
for x in range(100):
    for y in range(50):
        im.putpixel((x, y), (210, 210, 210))

# paint dark grey
for x in range(100):
    for y in range(50, 100):
        im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))

# confirm the color
px1 = im.getpixel((0, 0))
px2 = im.getpixel((0, 50))

print(f'pixel 0,0 : {px1}')
print(f'pixel 0,50 : {px2}')

im.save('putPixel.png')
