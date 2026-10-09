import requests

url = 'https://forum.astrio31.repl.co/api/v1/posts/1'
res = requests.get(url)

print(res.json())