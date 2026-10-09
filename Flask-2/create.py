import requests
from faker import Faker
from random import choice, randint

fake = Faker()

categories = ['sport', 'clothing', 'food', 'cars', 'shoes', 'school']

url = 'https://Flask-2.astrio31.repl.co/api/products'

for i in range(100):
  data = {
    'name': fake.name(),
    'brand': fake.company(),
    'category': choice(categories),
    'price': randint(10, 3000)
  }

  requests.post(url, json=data)