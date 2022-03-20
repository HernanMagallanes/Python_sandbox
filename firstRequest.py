# Downloading files from web with the request module
import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

print(f'type: {type(res)}')
print(f'code ok: {res.status_code == requests.codes.ok}')
print(f'len: {len(res.text)}')
print('\ntext: ')
print(res.text[:250])

# checking for errors
print('\nraise status errors : ')
res = requests.get('https://automatetheboringstuff.com/page_that_not_exits')

try:
    res.raise_for_status()

except Exception as exc:
    print('There  was a promblem: %s' % exc)
