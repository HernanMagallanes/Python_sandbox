# Renaming files with american-style dates to european-style dates

import os
import re
import shutil

# Step 1: create a regex for american-style dates

datePattern = re.compile(r'''
^(.*?)          # all text before the date
((0|1)?\d)-     # one or two digits for the month
((0|1|2|3)?\d)- # one or two digits for the day
((19|20)\d\d)   # four digits for the year
(.*?)$          # all text after the date
''', re.VERBOSE)

# Step 2: identify the date parts from filenames

for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    if mo is None:
        continue

    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Step 3: from the new filename and rename the files
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    print(f'Renaming {amerFilename}')
    print(f'to {euroFilename} ...')

    # shutil.move(amerFilename, euroFilename)
