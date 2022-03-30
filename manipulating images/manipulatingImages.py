# Cropping images

from PIL import Image

catIm = Image.open('zophie.png')

# Coordinates and box tuples
# (0,0) -> (x,0)
# (0,y) -> (x,y)

# (x_left, y_top, x_right +1 , y_bottom +1 )

croppedIm = catIm.crop((335, 345, 565, 560))
croppedIm.save('cropped.png')
