# draw on images

from PIL import Image, ImageDraw

im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)

# drawing shapes

# points(xy, fill)
for i in range(150, 200, 5):
    for j in range(150, 200, 5):
        draw.point([i, j], fill='black')

# line(xy, fill, width)
draw.line([(0, 0), (199, 0), (0, 199), (0, 0)], fill='black')

# rectangle(xy, fill, outline)
draw.rectangle((20, 30, 60, 60), fill='blue')

# ellipse(xy, fill, outline)
draw.ellipse((120, 30, 190, 60), fill='red')

# polygon(xy, fill, outline)
draw.polygon((
    (57, 87), (79, 62), (94, 85), (120, 90), (103, 113)),
    fill='brown')

for i in range(100, 200, 10):
    draw.line([(i, 0), (200, i - 100)], fill='green')

im.save('drawing.png')
