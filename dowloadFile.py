# Saving Downloaded files to the hard drive
import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()

# wb: web binary
playFile = open('RomeoAndJuliet.txt', 'wb')

for chunk in res.iter_content(100_000):
    playFile.write(chunk)

playFile.close()
