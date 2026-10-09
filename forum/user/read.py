import requests

with open('token.txt', 'r', encoding='utf-8') as file:
  token = file.read()

url = 'https://forum.astrio31.repl.co/api/v1/user'

res = requests.get(url, headers={
  'Authorization': f'Bearer {token}'
})

print(res.json())