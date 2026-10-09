import requests

with open('token.txt') as file:
  token = file.read()

url = 'https://forum.astrio31.repl.co/api/v1/posts/1'

posts = {
  'post_name': 'First post!!!!',
  'post_content': '13456789',
}

res = requests.put(url, json=posts, headers={
  'Authorization': f'Bearer {token}'
})

print(res.json())