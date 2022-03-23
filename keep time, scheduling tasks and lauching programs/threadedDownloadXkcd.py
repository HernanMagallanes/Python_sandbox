# Multithreaded XKCD Downloader

import threading
import requests
import bs4
import os

# Step 1: Modify the program to use a function

os.makedirs('xkcd', exist_ok=True)


def download_xkcd(start_comic, end_comic):
    for urlNumber in range(start_comic, end_comic):
        print('Downloading page https://xkcdc.com/%s...' % urlNumber)

        res = requests.get('https://xkcd.com/%s' % urlNumber)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        comic_elem = soup.select('#comic img')

        # if comic_elem == []:
        if not comic_elem:

            print('Could not find comic image.')

        else:
            comic_url = comic_elem[0].get('src')
            print('Downloading image %s...' % comic_url)

            res = requests.get('https:' + comic_url)
            res.raise_for_status()

            image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')

            for chunk in res.iter_content(100_000):
                image_file.write(chunk)

            image_file.close()


# Step 2: Create and start threads

downloadThreads = []

for i in range(0, 30, 5):
    start = i
    end = i + 4

    if start == 0:
        start = 1

    downloadThread = threading.Thread(target=download_xkcd,
                                      args=(start, end))

    downloadThreads.append(downloadThread)
    downloadThread.start()

# Step 3: Wait for all threads to end

for downloadThread in downloadThreads:
    downloadThread.join()

print('Done.')
