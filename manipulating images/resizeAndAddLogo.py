# Adding a logo

from PIL import Image
import os

import reshapingLogo


def add_logo():
    try:
        # Step 1: Open the logo image
        SQUARE_FIT_SIZE = 300
        LOGO_FILENAME = 'shrinkCatLogo.png'

        logoIm = Image.open(LOGO_FILENAME)

        logoWidth, logoHeight = logoIm.size

        # Step 2: Loop over all files and open images
        FOLDER_NAME = 'images_with_logo'
        os.makedirs(FOLDER_NAME, exist_ok=True)

        for filename in os.listdir('.'):

            if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILENAME:
                continue

            im = Image.open(filename)
            width, height = im.size

            # Step 3: Resize the images

            if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
                if width > height:
                    height = int((SQUARE_FIT_SIZE / width) * height)
                    width = SQUARE_FIT_SIZE
                else:
                    width = int((SQUARE_FIT_SIZE / height) * width)
                    height = SQUARE_FIT_SIZE

                print('Resizing %s...' % filename)
                im = im.resize((width, height))

            # Step 4: Add the logo and save the changes

            print('Adding logo to %s...' % filename)
            im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
            # im.paste(logoIm, (-(width - logoWidth), - (height - logoHeight)), logoIm)

            print('images sizes :')
            print(f'img : width {width} , height {height}')
            print(f'logo : width {logoWidth} , height {logoHeight}')
            print(f'paste point: {width - logoWidth} , {height - logoHeight}')

            im.save(os.path.join(FOLDER_NAME, filename))

            pass

    except Exception as err:
        print(err)


if __name__ == '__main__':
    add_logo()
