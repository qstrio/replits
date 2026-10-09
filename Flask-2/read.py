import requests

url = 'https://Flask-2.astrio31.repl.co/api/product/4'

res = requests.get(url)
print(res.json())