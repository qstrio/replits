import sqlite3
from random import randint

connection = sqlite3.connect('grades.db')
cursor = connection.cursor()

# sql = '''
#   CREATE TABLE grades(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     grade INT NOT NULL
#   )
# '''

# cursor.execute(sql)

# for i in range(100):
#   sql = f'''
#     INSERT INTO grades(grade)
#     VALUES ({randint(50, 100)})
#   '''

#   cursor.execute(sql)
#   connection.commit()

sql = '''
  SELECT id, MAX(grade) FROM grades
'''

sql = '''
  SELECT id, MIN(grade) FROM grades
'''

sql = '''
  SELECT * FROM grades
  ORDER BY grade DESC
'''

sql = '''
  SELECT * FROM grades
  ORDER BY grade ASC
  LIMIT 10
'''

cursor.execute(sql)
rows = cursor.fetchall()

# max_grade = 0
# for row in rows:
#   if row[1] > max_grade:
#     max_grade = row[1]
# print(max_grade)

for row in rows:
  print(row)