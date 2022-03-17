# Backing a folder into a ZIP file

# copies an entire folder and its contents
# into a ZIP file whose filename increments

import os
import zipfile
from pathlib import Path


def backup_to_zip(folder):
    # folder = os.path.abspath(folder)

    # Step 1: figure out the ZIP file's name
    p = Path.cwd()
    folder = os.path.join(p, str(folder))

    n = 1

    while True:
        zip_filename = os.path.basename(folder) + '_' + str(n) + '.zip'

        if not os.path.exists(zip_filename):
            break
        n += 1

    # Step 2: create the new ZIP file

    print(f'\n Creating {zip_filename} ...')
    backup_zip = zipfile.ZipFile(zip_filename, 'w')

    # Step 3: walk the directory and add to the ZIP file

    for foldername, subfolders, filenames in os.walk(folder):
        print(f'\n Adding files in  ... ')
        print(foldername)
        backup_zip.write(foldername)

        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue
            backup_zip.write(os.path.join(foldername, filename))

    backup_zip.close()
    print('Done.')


backup_to_zip('TEST')
