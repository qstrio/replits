cimport sqlite3
from faker import Faker
from random import randint

connection = sqlite3.connect('students.db')
cursor = connection.cursor()
fake = Faker()

# sql = '''
#   CREATE TABLE students(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name CHAR(125) NOT NULL,
#     math INT NOT NULL,
#     english INT NOT NULL,
#     french INT NOT NULL,
#     grade INT NOT NULL
#   )
# '''

# sql = '''
#   CREATE TABLE sales(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     price INT NOT NULL
#   )
# '''

# cursor.execute(sql)

# for i in range(500):
#   price = randint(1, 100)

#   sql = f'''
#     INSERT INTO sales(price)
#     VALUES ({price})
#   '''

#   cursor.execute(sql)
#   connection.commit()

sql = '''
  SELECT AVG(french) FROM students
  WHERE grade = 8
'''

sql = '''
  SELECT SUM(price) FROM sales
'''

sql = '''
  SELECT COUNT(math) FROM students
  WHERE math >= 90 AND grade = 6
'''

sql = '''
  SELECT COUNT(name) FROM students
  WHERE grade = 5
'''

sql = '''
  SELECT grade, COUNT(grade) FROM students
  GROUP BY grade
'''

sql = '''
  SELECT math, COUNT(math) FROM students
  WHERE math >= 90 AND grade = 1
  GROUP BY math
  ORDER BY COUNT(math)
'''


'''
Homework:
'''

# Question 1: Find the average of the french grade from the students table
sql = '''
  SELECT AVG(french) FROM students
'''

# Question 2: Find the average of the english grade for the grade 3 students

sql = '''
  SELECT AVG(english) FROM student
  WHERE grade = 3
'''

# Question 2.5: Find the average of the sales from the sales table

sql = '''
  SELECT AVG(price) FROM sales
'''

# Question 3: Find the sum of the sales from the sales table
sql = '''
  SELECT SUM(price) FROM sales
'''
# Question 4: count how many students have 80% in grade 1
sql = '''
  SELECT COUNT(name) FROM students
  WHERE math = 80 AND grade = 1
'''
# Question 5: count how products are sold that is greate than 50$ from the sales table

sql = '''
  SELECT COUNT(id) FROM sales
  WHERE price > 50
'''

# Question 6: count how many students where the math, french, and english is greater than 90%
sql = '''
  SELECT COUNT(name) FROM students
  WHERE math > 90 AND french > 90 AND english > 90
'''
# Question 7: count how many students where the math, french, and english is greater than 90% where the grade is 5

sql = '''
  SELECT COUNT(name) FROM students
  WHERE math > 90 AND french > 90 AND english > 90 AND grade = 5
'''
# Question 8: Display the count of the number of the students that their math is greater than 70% according to each grade

sql = '''
  SELECT grade, COUNT(name) FROM students
  WHERE math > 70
  GROUP BY grade
'''

# Question 9: Display the count of the math, french, and english is between 80% and 100% according to each grade

sql = '''
  SELECT grade, COUNT(name) FROM students
  WHERE math BETWEEN 80 AND 100 AND french BETWEEN 80 AND 100 AND english BETWEEN 80 AND 100
  GROUP BY grade
'''
# Bonus Question 1: Dispplay the average of math, english, and french

sql = '''
  SELECT AVG(math), AVG(english), AVG(french) FROM students
'''
# Bonus Question 2: Display the average of math, english and french according to each grade

sql = '''
  SELECT grade, AVG(math), AVG(english), AVG(french) FROM students
  GROUP BY grade
'''

cursor.execute(sql)
rows = cursor.fetchall()


for row in rows:
  print(row)