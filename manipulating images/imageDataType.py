# working with the image data type

from PIL import Image

catIm = Image.open('zophie.png')

print('\nimage...')

width, height = catIm.size

print(f'width: {width}')
print(f'height: {height}')

print(f'file name: {catIm.filename}')
print(f'format: {catIm.format}')
print(f'description: {catIm.format_description}')

# change format
catIm.save('zophie.jpg')

# new image
print('new images ...')

im = Image.new('RGBA', (100, 200), 'purple')
im.save('purpleImage.png')

# invisible black, default color if no color arg is specified
im = Image.new('RGBA', (20, 20))
im.save('transparentImage.png')
