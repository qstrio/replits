from faker import Faker
import sqlite3

connection = sqlite3.connect('user.db')
cursor = connection.cursor()

# sql = '''
#   CREATE TABLE user(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name CHAR(255) NOT NULL,
#     age INT NOT NULL,
#     country CHAR(125) NOT NULL,
#     address VARCHAR(300) NOT NULL,
#     birthday DATE
#   )
# '''

# cursor.execute(sql)

fake = Faker()

# for i in range(100):
#   name = fake.name()
#   birthday = fake.date()
#   age = 2023 - int(birthday[:4]) 
#   country = fake.country()
#   address = fake.address()

#   sql = f'''
#     INSERT INTO user(name, age, country, address, birthday)
#     VALUES ('{name}', {age}, '{country}', '{address}', '{birthday}')
#   '''

#   cursor.execute(sql)
#   connection.commit()

'''
UPDATE
'''
# sql = '''
#   UPDATE user
#   SET name = 'David Bob'
#   WHERE id = 2
# '''

# sql = '''
#   UPDATE user
#   SET name = 'Nicole Bob'
#   WHERE name = 'Nicole Brown' AND age = 36 AND country = 'Gabon' AND birthday = '1987-12-13'
# '''

# sql = '''
#   UPDATE user
#   SET age = 20, birthday = '2003-05-25'
#   WHERE id = 30
# '''

# cursor.execute(sql)
# connection.commit()

'''
DELETE
'''

# sql = '''
#   DELETE FROM user
#   WHERE id = 15
# '''

# cursor.execute(sql)


'''
Homework:
'''

# Question 1: randomly update the user's country

sql = f'''
  UPDATE user
  SET country = '{fake.country()}'
  WHERE id = 8
'''

# Question 2: randomly update the user's birthday and the age

sql = '''
  UPDATE user
  SET birthday = '1998-02-14', age = 25
'''

# Question 3: randomly update the user's name, age, birthday, and address

name1 = fake.name()
address1 = fake.address()

sql = '''
  UPDATE user
  SET name = name1, address = address1, age = 15 , birthday = '2007-11-09'
  WHERE id = 23
'''

# Question 4: delete the user based on one random country

country1 = fake.country()
sql = f'''
  DELETE FROM user 
  WHERE country = '{country1}'
'''

# Question 5: delete the user if the age is 90

sql = '''
  DELETE FROM user
  WHERE age = 90
'''

# Question 6: delete the user if age is below 12 

sql = '''
  DELETE FROM user
  WHERE age < 12
'''
# Question 7: delete the user if age is 50 and the country is Canada

sql = '''
  DELETE FROM user
  WHERE age = 50 AND country = 'Canada'
'''

cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
  print(row)