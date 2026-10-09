import requests

url = 'https://hospital-server.astrio31.repl.co/api/hospitals'


data = [
  {
    'name': 'Orange County Global Medical Center',
    'address': '1001 N Tustin Ave, Santa Ana',
    'category': 'General Hospital',
    'distance': 700,
    'website': 'orangecountyglobalmedicalcenter.com'
  },
  {
    'name': 'Centura Porter Adventist Hospital',
    'address': '2525 S Downing ST, Denver',
    'category': 'General Hospital',
    'distance': 300,
    'website': 'centura.org'
  },
  {
    'name': 'Paramount Pediatrics',
    'address': '15336 31st Ave, Surrey',
    'category': 'Pediatrics',
    'distance': 162,
    'website': 'paramountpediatrics.com'
  },
  {
    'name': 'Quality Medical Imaging',
    'address': '0835, 2460 Professional Ct # 110, Las Vegas',
    'category': 'X-ray lab',
    'distance': 206,
    'website': 'qualitymedicalimaging.org'
  }
]

for hospital in data:
  requests.post('https://hospital-server.astrio31.repl.co/api/hospital/create', json=hospital)