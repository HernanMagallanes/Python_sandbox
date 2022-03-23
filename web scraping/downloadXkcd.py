# Download XKCD comics

# request - downloads files and web pages
# bs4 - parses HTML

import requests
import bs4
import os

# Step 1: Design the program

url = 'https://xkcd.com'

# store comics in folder
os.makedirs('xkcd', exist_ok=True)

for i in range(10):
    # Step 2: Download teh web page

    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Step 3: Find and download the comic image

    comicElem = soup.select('#comic img')
    if not comicElem:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Step 4: Save the image and find the previous comic

        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')

        for chunk in res.iter_content(100_000):
            imageFile.write(chunk)
        imageFile.close()

    prevLink = soup.select('a[rel=prev]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done')
