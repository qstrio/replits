import requests

url = 'https://flask-3.astrio31.repl.co/api/user'
user = {
  'first_name': 'David',
  'last_name': 'Steve'
}

with open('token.txt', 'r', encoding='utf-8') as file:
  token = file.read()


res = requests.put(url, json=user, headers={
  'Authorization': f'Bearer {token}'
})
print(res.json())