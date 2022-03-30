# Colors and RGBA values
# Python Imaging Library

from PIL import ImageColor

r = ImageColor.getcolor('red', 'RGBA')
g = ImageColor.getcolor('lime', 'RGBA')
b = ImageColor.getcolor('blue', 'RGBA')

print(r)
print(g)
print(b)

w = ImageColor.getcolor('white', 'RGBA')
bc = ImageColor.getcolor('black', 'RGBA')

print(w)
print(bc)

