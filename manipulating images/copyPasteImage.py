# Copying and pasting images onto other images

catCopyIm = catIm.copy()

faceIm = catIm.crop((335, 345, 565, 560))
print(f'image size: {faceIm.size}')

catCopyIm.paste(faceIm, (0, 0))
catCopyIm.paste(faceIm, (400, 500))

catCopyIm.save('pasted.png')
