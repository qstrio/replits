import requests

url = 'https://flask-3.astrio31.repl.co/api/user/login'


user = {
  'email': 'bobbobs@jobsbob.com',
  'password': 'cats123'
}

res = requests.post(url, json=user)

with open('token.txt', 'w', encoding='utf-8') as file:
  token = res.json()['token']
  file.write(token)
