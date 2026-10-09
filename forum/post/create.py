import requests

with open('token.txt') as file:
  token = file.read()

url = 'https://forum.astrio31.repl.co/api/v1/posts/create'

posts = {
  'post_name': 'First post!!!!',
  'post_content': 'slfkdsafj',
  'category_id': 1
}

res = requests.post(url, json=posts, headers={
  'Authorization': f'Bearer {token}'
})

print(res.json())