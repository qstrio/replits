import requests

data = {
  'experience': 9,
  'title': 'Senior Musician'
}

url = 'https://flask-3.astrio31.repl.co/api/job/1'

with open('token.txt') as file:
  token = file.read()



res = requests.put(url, json=data, headers={
  'Authorization': f'Bearer {token}'
})
print(res.json())