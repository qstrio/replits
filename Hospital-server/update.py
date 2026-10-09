import requests

url = 'https://hospital-server.astrio31.repl.co/api/hospital/2'

data = {
  'name': 'Saint Francis Memorial Hospital',
  'address': '900 Hyde St, San Francisco',
  'category': 'General Hospital',
  'distance': 709,
  'website': 'locations.dignityhealth.org'
}

requests.put(url, json=data)