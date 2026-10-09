import requests

url = 'https://flask-3.astrio31.repl.co/api/user/1'

res = requests.delete(url)
print(res.json)