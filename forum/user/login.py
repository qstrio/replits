import requests

user = {
  'email': 'Bobjobs@forum.ca',
  'password': '13579'
}

user = {
  'email': 'admin@forum.ca',
  'password': '13579'
}

url = 'https://forum.astrio31.repl.co/api/v1/user/login'

res = requests.post(url, json=user)
token = res.json()['token']


with open('token.txt', 'w', encoding='utf-8') as file:
  file.write(token)