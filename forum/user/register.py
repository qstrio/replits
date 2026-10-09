import requests

user = {
  'email': 'Bobjobs@forum.ca',
  'password': '13579',
  'name': 'Bob',
  'birth': '1576-08-23',
  'country': 'Romania'
}

url = 'https://forum.astrio31.repl.co/api/v1/user/register'

res = requests.post(url, json=user)
print(res.json())