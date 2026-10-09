import sqlite3
from faker import Faker
from random import randint

connection = sqlite3.connect('sql4.db')
cursor = connection.cursor()
fake = Faker()

# sql = '''
#   CREATE TABLE user(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name CHAR(255) NOT NULL,
#     email CHAR(255) NOT NULL
#   )
# '''

# cursor.execute(sql)

# sql = '''
#   CREATE TABLE orders(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     amounts INTEGER NOT NULL,
#     order_date DATE NOT NULL,
#     user_id INTEGER,
#     FOREIGN KEY(user_id) REFERENCES user(id)
#   )
# '''

# cursor.execute(sql)

# for i in range(20):
#   name = fake.name()
#   email = fake.email()

#   sql = f''' 
#     INSERT INTO user(name, email)
#     VALUES ('{name}', '{email}')
#   '''

#   cursor.execute(sql)
#   connection.commit()


for i in range(100):
  amounts = randint(20, 500)
  order_date = fake.date()
  user_id = randint(1, 20)
  
  sql = f''' 
    INSERT INTO orders(amounts, order_date, user_id)
    VALUES ('{amounts}', '{order_date}', {user_id})
  '''

  cursor.execute(sql)
  connection.commit()
  



# sql = '''
#   SELECT * FROM orders
# '''

sql = '''
  SELECT user.name, user.email, orders.amounts, orders.order_date FROM user
  INNER JOIN orders ON user.id = orders.user_id
  WHERE user.name = 'Adam Hall' AND orders.amounts > 300
'''

# Question 1: join the table and query name from user table, amounts from the order table
sql = '''
  SELECT user.name, orders.amounts FROM user
  INNER JOIN orders ON user.id = orders.user_id
'''
# Question 2: join the table and query name, email from user table, amounts, order_date FROM order table
# WHERE the user.id is 15

sql = '''
  SELECT user.name, user.email, orders.amounts, orders.order_date FROM user 
  INNER JOIN orders ON user.id = orders.user_id
  WHERE user.id = 15
'''
# Question 3: join the table and query name, email from user table, amounts, order_date FROM order table
# WHERE the user.id is 10 and the amounts is less than 200

sql = '''
  SELECT user.name, user.email, orders.amounts, orders.order_date FROM user
  INNER JOIN orders ON user.id = orders.user_id
  WHERE user.id = 10 AND orders.amounts < 200
'''
# Question 4: join the table and query name, email from user table, amounts, order_date FROM order table
# WHERE the user.id is 5 and the amounts greater than or equal 299

sql = '''
  SELECT user.name, user.email, orders.amounts, orders.order_date FROM user
  INNER JOIN orders ON user.id = orders.user_id
  WHERE user.id = 5 AND orders.amounts >= 299
'''

# Question 5: join the table and query name, email from user table, amounts, order_date FROM order table
# WHERE the amounts is less than or equal to 100

sql = '''
  SELECT user.name, user.email, orders.amounts, orders.order_date FROM user
  INNER JOIN orders ON user.id = orders.user_id
  WHERE orders.amounts <= 100
'''

# Question 6: join the table and query name, email from user table, amounts, order_date FROM order table
# WHERE the the amounts is between 200 and 300

sql = '''
  SELECT user.name, user.email, orders.amounts, orders.order_date FROM user
  INNER JOIN orders ON user.id = orders.user_id
  WHERE orders.amounts BETWEEN 200 AND 300
'''


cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
  print(row)