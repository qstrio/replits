import requests

data = {
  'title': 'Professor',
  'exp': 5,
  'company': 'UBC',
  'user_id': 1
}

url = 'https://flask-3.astrio31.repl.co/api/job/create'

with open('token.txt') as file:
  token = file.read()

res = requests.post(url, json=data, headers={
  'Authorization': f'Bearer {token}'
})

print(res.json())
