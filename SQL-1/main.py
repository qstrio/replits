import sqlite3

connection = sqlite3.connect('tut.db')

cursor = connection.cursor()

# sql = '''
#   CREATE TABLE user(
#     id INTEGER PRIMARY KEY AUTOINCREMENT, 
#     name CHAR(255),
#     email CHAR(255),
#     password CHAR(64)
#   )
# '''

# sql = '''
#   INSERT INTO user(name, email, password)
#   VALUES 
#     ('Sarah', 'sarah@gmail.com', '1234567890'),
#     ('James', 'james@hotmail.com', '55555555')
# '''

# cursor.execute(sql)
# connection.commit()

# sql = '''
#   SELECT * FROM user
# '''

# cursor.execute(sql)

# rows = cursor.fetchall()

# for row in rows:
#   print(row)


'''
Create a city table
id, name, province, country
'''


'''
INSERT 5 records to the table
'''


'''
SELECT everything from the table
and print it out
'''

sql = '''
  CREATE TABLE city(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name CHAR(255),
    province CHAR(255),
    country CHAR(255)
  
  )
'''

cursor.execute(sql)

sql = '''
  INSERT INTO city(name, province, country)
  VALUES
    ('Vancouver', 'British Columbia', 'Canada'),
    ('Shanghai', 'Shanghai Province', 'China'),
    ('Alientown', 'Alien Province', 'Alpha Centauri'),
    ('New York', 'New York', 'USA'),
    ('Ottawa', 'Ontario', 'Canada')
  
'''

cursor.execute(sql)
connection.commit()
sql = '''
SELECT * FROM city
'''
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
  print(row)