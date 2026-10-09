import requests

with open('token.txt') as file:
  token = file.read()

url = 'https://forum.astrio31.repl.co/api/v1/category/create'

for name in ['physics', 'chemistry', 'biology']:
  subject = {
    'name': name
  }
  res = requests.post(url, json=subject, headers={
    'Authorization': f'Bearer {token}'
  })

print(res.json())