import requests

url = 'https://forum.astrio31.repl.co/api/v1/comments/1'

res = requests.get(f'{url}?page=1')

print(res.json())