# Resizing an image

from PIL import Image

catIm = Image.open('Zophie.png')

width, height = catIm.size

# shrink the image
quarter_sized_img = catIm.resize((int(width / 2), int(height / 2)))
quarter_sized_img.save('quarter_sized.png')

# stretch the image
svelte_img = catIm.resize((width, height + 200))
svelte_img.save('svelte.png')
