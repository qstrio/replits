import requests

url = 'https://forum.astrio31.repl.co/api/v1/user/1/posts'

res = requests.get(url)

print(res.json())