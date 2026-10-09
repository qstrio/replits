import requests

with open('token.txt') as file:
  token = file.read()

url = 'https://forum.astrio31.repl.co/api/v1/posts/1'

res = requests.delete(url, headers={
  'Authorization': f'Bearer {token}'
})

print(res.json())