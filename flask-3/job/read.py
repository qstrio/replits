import requests

url = 'https://flask-3.astrio31.repl.co/api/job/1'

with open('token.txt') as file:
  token = file.read()

res = requests.get(url, headers={
  'Authorization': f'Bearer {token}'
})

print(res.json())