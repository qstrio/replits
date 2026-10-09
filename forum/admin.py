import sqlite3
from hashlib import sha256
import os

connection = sqlite3.connect('instance/forum.db')
cursor = connection.cursor()

pw = sha256()
pw.update(os.environ['SALT'].encode())
pw.update(b'13579')
print(pw.hexdigest())
sql = f'''
  INSERT INTO user(email, password, name, role, registration, active)
  VALUES ("admin@forum.ca", "{pw.hexdigest()}", "admin", "admin", "2023-07-10 23:09:59.052487", 0)
'''

cursor.execute(sql)
connection.commit()