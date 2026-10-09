import requests

with open('token.txt', 'r', encoding='utf-8') as file:
  token = file.read()

url = 'https://forum.astrio31.repl.co/api/v1/user'

data = {
  'name': 'Bobobobobos',
  'birth': '3412-03-27',
  'country': 'Mars'
}

res = requests.put(url, headers={
  'Authorization': f'Bearer {token}'
},json=data)

print(res.json())