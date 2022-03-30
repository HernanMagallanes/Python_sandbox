from PIL import Image


def main():
    try:

        LOGO_FILENAME = 'catlogo.png'

        logoIm = Image.open(LOGO_FILENAME)

        logoWidth, logoHeight = logoIm.size

        # shrink the image
        n = 8
        shrink_logo = logoIm.resize((int(logoWidth / n), int(logoHeight / n)))
        # logoWidth, logoHeight = shrink_logo.size

        print('new logo: OK')

        shrink_logo.save('shrinkCatLogo.png')

    except Exception as err:
        print(str(err))


main()
