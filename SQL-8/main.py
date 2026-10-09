Cimport sqlite3
from faker import Faker

connection = sqlite3.connect('user.db')
cursor = connection.cursor()
fake = Faker()

# sql = '''
#   CREATE TABLE user(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     first_name CHAR(125) NOT NULL,
#     last_name CHAR(125) NOT NULL,
#     country CHAR(255) NOT NULL
#   )
# '''

# cursor.execute(sql)

# for i in range(500):
#   first_name = fake.first_name()
#   last_name = fake.last_name()
#   country = fake.country()

#   sql = f'''
#     INSERT INTO user(first_name, last_name, country)
#     VALUES ("{first_name}", "{last_name}", "{country}")
#   '''

#   cursor.execute(sql)

# connection.commit()

sql = '''
  SELECT COUNT(DISTINCT(first_name)) FROM user
'''

sql = '''
  SELECT COUNT(first_name) FROM user
  WHERE first_name NOT IN ('Sarah', 'Michael', 'Robert')
'''

sql  = '''
  SELECT * FROM user
  WHERE first_name in ('Sarah', 'Michael', 'Robert')
'''

# Question 1: query the unique countries 

sql = '''
  SELECT DISTINCT(country) FROM user
'''

# Question 2: count how many unique countries

sql = '''
  SELECT COUNT(DISTINCT(country)) FROM user
'''

# Question 3: query the unique last name

sql = '''
  SELECT DISTINCT(last_name) FROM user
'''

# Question 4: count how many unique last name

sql = '''
  SELECT COUNT(DISTINCT(last_name)) FROM user
'''

# Question 5: query how many people are living in Mexico, Malta, Spain, and Thailand

sql = '''
  SELECT COUNT(id) FROM user
  WHERE country in ('Mexico', 'Malta', 'Spain', 'Thailand')
'''

# Question 6: query how many people are not living in Chile, Iceland, and Korea

sql = '''
  SELECT COUNT(id) FROM user
  WHERE country NOT IN ('Chile', 'Iceland', 'Korea')
'''
# Question 7: Count how many people are living in each country

sql = '''
  SELECT country, COUNT(id) FROM user
  GROUP BY country
'''

# Question 8: Count how many people have the same last name

sql = '''
  SELECT last_name, COUNT(id) FROM user
  GROUP BY last_name
'''

# Quesiton 9: Count how many peole's first name Robert are living in Iceland


sql = '''
  SELECT COUNT(id) FROM user
  WHERE first_name is 'Robert' AND country = 'Iceland'
'''

# Bonus: What is percentage of people living in Iceland among the databse

sql = '''
  SELECT * FROM user
  WHERE country = 'Iceland'
'''



cursor.execute(sql)
rows = cursor.fetchall()


percentage = round((len(rows) / 1500) * 100, 2)
print(f'{percentage}%')


# for row in rows:
#   print(row)