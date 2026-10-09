import requests

url = 'https://hospital-server.astrio31.repl.co/api/hospital/longest'

res = requests.get(url)
print(res.json())