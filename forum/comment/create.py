import requests

url = 'https://forum.astrio31.repl.co/api/v1/comments/create'

with open('token.txt') as file:
  token = file.read()

comment = {
  'comment_content': 'This article is cool',
  'post_id': 1
}

res = requests.post(url, json=comment, headers={
  'Authorization': f'Bearer {token}'
})

print(res.json())