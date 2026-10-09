import requests

url = 'https://Flask-2.astrio31.repl.co/api/product/4'

data = {
  'brand': 'Adidas'
}

requests.put(url, json=data)