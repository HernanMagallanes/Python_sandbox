# Parsing HTML with the bs4 module

# beautifulSoup object
import requests
import bs4

res = requests.get('https://nostarch.com/')
res.raise_for_status()

noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
print(f'type: {type(noStarchSoup)}')

# find element with select()
# with a string like CSS selector

exFile = open('example.html')
exSoup = bs4.BeautifulSoup(exFile, 'html.parser')
elems = exSoup.select('#author')

print(type(elems))
print(len(elems))

print(type(elems[0]))
print(str(elems[0]))

print(elems[0].getText())
print(elems[0].atrrs)

# getting data from element's attributes
print(elems.get('id'))
