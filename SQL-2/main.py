import sqlite3

connection = sqlite3.connect('tut.db')
cursor = connection.cursor()

# sql = '''
#   CREATE TABLE user(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name CHAR(125) NOT NULL,
#     email CHAR(125) NOT NULL UNIQUE,
#     password CHAR(125) NOT NULL,
#     age INT,
#     gender CHAR(100) 
#   )
# '''

# sql = '''
#   INSERT INTO user(name, email, password, age, Gender)
#   VALUES 
#     ('Angie', 'angie@gmail.com', '123456789', 22, 'Female'),
#     ('Michael', 'michael@gmail.com', 'fasfhkgjsdagfjhdsgjfhs', 35, 'Male')
# '''

# cursor.execute(sql)
# connection.commit()


# sql = '''
#   SELECT name, email, age, gender FROM user
#   WHERE age IS NULL
# '''

# sql = '''
#   SELECT name, email, age, gender FROM user
#   WHERE age IS NOT NULL
# '''

# sql = '''
#   SELECT name, email, age, gender FROM user
#   WHERE gender IS NULL
# '''

# sql = '''
#   SELECT name, email, age, gender FROM user
#   WHERE age BETWEEN 20 AND 40
# '''

# sql = '''
#   SELECT name, email, age, gender FROM user
#   WHERE age > 20 AND gender = 'Male'
# '''

# sql = '''
#   SELECT name, email, age, gender FROM user
#   WHERE age < 20 OR gender IS NULL
# '''

# cursor.execute(sql)
# rows = cursor.fetchall()

# for row in rows:
#   print(row)

'''
Homework
'''

# make a student with 5 columns,  id
# requirment, use at least one NOT NULL clause and one UNIQUE clause in the table creation

# sql = '''
#   CREATE TABLE student(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name CHAR(125) NOT NULL,
#     email CHAR(125) NOT NULL UNIQUE, 
#     age INT,
#     grade INT NOT NULL,
#     gender CHAR(100)
#   )

# '''
# cursor.execute(sql)

# insert 5 students into the the table
# sql = '''
#   INSERT INTO student(name, email, age, grade, gender)
#   VALUES
#   ('Kiana', 'kiana@gmail.com', 16, 11, 'female'),
#   ('James', 'james@gmail.com', 14, 9, 'male'),
#   ('Emily', 'emily@hotmail.com', 17, 12, 'female'),
#   ('Catherine', 'cathy@gmail.com', 13, 8, 'female'),
#   ('Joe', 'joe@hotmail.com', 15, 10, 'male')
# '''
# cursor.execute(sql)
# connection.commit() 


# Query

# Question 1: select everything from the student table
sql = '''
  SELECT * FROM student
'''

# Question 2: select 3 columns from the student table

sql = '''
  SELECT name, age, email FROM student 
'''

# Question 3: select 3 columns from the student table where grade is greater than 4

sql = '''
  SELECT age, email, grade FROM student 
  WHERE grade > 4
'''
# Question 4: select 3 columns from the student table where age is between 13 and 16 years old

sql = '''
  SELECT name, gender, email FROM student 
  WHERE age BETWEEN 13 AND 16
'''

# Question 5: select 3 columns from the student table where age is 15 years old and grade is greater than or equal to 1

sql = '''
  SELECT age, gender, email FROM student
  WHERE age IS 15 AND grade >= 1
'''
# Question 6: select 3 columns from the student table where age is 17 years old or grade is 12 

sql = '''
  SELECT name, gender, email FROM student
  WHERE age IS 17 OR grade IS 12
'''

# Question 7: select 3 columns from the student table where age is 13 and the geder is female

sql = '''
  SELECT name, grade, age FROM student
  WHERE age IS 13 AND gender = 'female'
'''

# Question 8: select 3 columns from the student table where gender is male
sql = '''
  SELECT name, email, grade FROM student
  WHERE gender = 'male'
'''

cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
  print(row)