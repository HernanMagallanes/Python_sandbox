# Multi-clipboard automatic messages

import sys
import pyperclip

# pyperclip.copy('Hello')
# pyperclip.paste()

# Step 1 - Program design and data structures

TEXT = {'agree': """Yes, I agree. That sounds fine to me. """,
        'busy': """Sorry, can we do this later this week or next week? """,
        'upsell': """Would you consider making this a monthly donations? """}
# Step 2 - Handle command line arguments

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase test')
    sys.exit()

keyphrase = sys.argv[1]

# Step 3 - Copy the right phrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for' + keyphrase + ' copied to clipboard')
else:
    print('there is no text for ' + keyphrase)
