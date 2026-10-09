import sqlite3 
from faker import Faker

connection = sqlite3.connect('address.db')
cursor = connection.cursor()

fake = Faker()

# sql = '''
#   CREATE TABLE address(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     street CHAR(350) NOT NULL,
#     postcode CHAR(125) NOT NULL,
#     country CHAR(125) NOT NULL
#   )
# '''

# cursor.execute(sql)

# for i in range(500):
#   street = fake.street_address()
#   postcode = fake.postcode()
#   country = fake.country()

#   sql = f'''
#     INSERT INTO address(street, postcode, country)
#     VALUES ("{street}", "{postcode}", "{country}")
#   '''

#   cursor.execute(sql)

# connection.commit()


sql = '''
  SELECT * FROM address
  WHERE street LIKE '%William%'
'''

sql = '''
  SELECT * FROM address
  WHERE street like '32%'
'''

sql = '''
  SELECT * FROM address
  WHERE street like '__2%'
'''

sql = '''
  SELECT * FROM address
  WHERE street like '%s__'
'''

sql = '''
  SELECT * FROM address
  WHERE street like '32%s'
'''


# Homework:

# Question 1: Find the street that starts with 2

sql = '''
  SELECT * FROM address
  WHERE street like '2%'
'''

# Question 2: Find the street that ends with o

sql = '''
  SELECT * FROM address
  WHERE street like '%o'
'''
# Question 3: Find the street that has main in it

sql = '''
  SELECT * FROM address
  WHERE street like '%Main%'
'''

# Question 4: Find the street that starts with 123

sql = '''
  SELECT * FROM address
  WHERE street like '123%'
'''
# Question 5: Find the street that starts with 24 and ends with y

sql = '''
  SELECT * FROM address 
  WHERE street like '24%y'
'''
# Question 6: Find the street where the third character is 3
sql = '''
  SELECT * FROM address
  WHERE street like '__3%'
'''
# Question 7: Find the street where the fourth last character is e

sql = '''
  SELECT * FROM address
  WHERE street like '%e___'
'''

# Question 8: Find the postcode where it starts with 1

sql = '''
  SELECT * FROM address 
  WHERE postcode like '1%'
'''

# Question 9: Find the postcode where it starts with 82

sql = '''
  SELECT * FROM address
  WHERE postcode like '82%'
'''

# Question 10: Find the post code where it ends with 9

sql = '''
  SELECT * FROM address
  WHERE postcode like '%9'
'''

# Question 11: Find the post code where second number is 2 and the second last number is 3

sql = '''
  SELECT * FROM address
  WHERE postcode like '_2%3_'
'''

# Bonus Question: Count how many streets starts with 23

sql = '''
  SELECT COUNT(id) FROM address
  WHERE street like '23%'
'''

# Bonus Question 2: Count how many postcode where the middle 3

sql = '''
  SELECT COUNT(id) FROM address
  WHERE postcode like '_%3%_'
'''

# Bonus Question 3: Count how many unique contries
sql = '''
  SELECT country FROM address
'''
cursor.execute(sql)
rows = cursor.fetchall()

countries = set()

for row in rows:
  countries.add(row[0])

print(len(countries))