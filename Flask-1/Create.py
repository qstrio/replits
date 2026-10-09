import requests

url = 'https://Flask-1.astrio31.repl.co/api'

student = {
  'name': 'Benjamin'
}

requests.post(f'{url}/student', json=student)