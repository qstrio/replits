import requests

url = 'https://flask-3.astrio31.repl.co/api/user'

with open('token.txt', 'r', encoding='utf-8') as file:
  token = file.read()

res = requests.get(url, headers={
  'Authorization': f'Bearer {token}'
})
print(res.json())