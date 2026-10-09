import requests

url = 'https://Flask-1.astrio31.repl.co/api'

student = {
  'name': 'Bob'
}

requests.put(f'{url}/student/1', json=student)