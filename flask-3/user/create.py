import requests

url = 'https://flask-3.astrio31.repl.co/api/user/create'
user = {
  'first_name': 'Bob',
  'last_name': 'Jobs',
  'email': 'bobbobs@jobsbob.com',
  'password': 'cats123'
}

res = requests.post(url, json = user)
print(res.json())