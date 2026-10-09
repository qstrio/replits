import requests

with open('token.txt') as file:
  token = file.read()

url = 'https://forum.astrio31.repl.co/api/v1/comments/1'

comment = {
  'comment_content': 'I edited this comment loolollolol'
}

res = requests.put(url, json=comment, headers={
  'Authorization': f'Bearer {token}'
})

print(res.json())