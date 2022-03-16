# multi-clipboard with command line arguments save clipboard and return

# save <keyword> - saves clipboard to keyword
# <keyword> - loads keyword to clipboard
# list - loads all keywords to clipboard
# delete <keyword> - deletes clipboard to keyword

# shelve dictionary-like object
# the values in a shelf can be essentially arbitrary Python objects

import shelve
import pyperclip
import sys

# Step 1: Comments and shelf setup

mcbShelf = shelve.open('mcb')

# Step 2: Save clipboard content with a keyword

if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()

    if sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
        print('deleted')



elif len(sys.argv) == 2:

    # Step 3:  List keywords and load a keyword's content

    if sys.argv[1].lower() == 'list':

        pyperclip.copy(str(list(mcbShelf.keys())))
        print('\t')

        for k in mcbShelf.keys():
            print(k, mcbShelf[k])

    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
