import requests

url = 'https://Flask-1.astrio31.repl.co/api'

res = requests.get(f'{url}/student/2') 

print(res.json())