# Opening all search results

import webbrowser
import requests
import bs4
import sys

# Step 1: Get the command line arguments and requests the search page

print('Searching...')
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Step 2: Find all the results

soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.select('.package-snippet')

# Step 3: Open web browsers for each result

numOpens = min(5, len(linkElems))

for i in range(numOpens):
    urlOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlOpen)
    webbrowser.open(urlOpen)
