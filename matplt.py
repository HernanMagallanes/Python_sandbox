# mapIt.py with the webbrowser module
# launches a map in the browser using an address from
# the command line or clipboard

import webbrowser
import pyperclip
import sys

# Step 1: figure out the URL
# https://www.google.com/maps/place/

# Ex: 870 valencia st, San francisco, CA 94110

# Step 2: handle the command line arguments

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])

else:
    # Step 3: handle the clipboard and launch the browser

    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
