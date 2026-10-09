# import the needed packages
# set up the database
# set up the hospital table
# set up the API Routes
# test

# https://imgur.com/a/kwRbPYn


from flask import Flask, request
import sqlite3

connection = sqlite3.connect('hospitals.db', check_same_thread=False)
cursor = connection.cursor()

sql = '''
  CREATE TABLE hospitals(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name CHAR(255) NOT NULL,
    address CHAR(255) NOT NULL,
    category CHAR(255) NOT NULL,
    distance INT(5) NOT NULL,
    website CHAR(255) 
  )
'''

# cursor.execute(sql)

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from Flask!'


@app.route('/api/hospital/create', methods=['POST'])
def createhospitals():
  if request.method == 'POST':
    data = request.json 
    try:
      name = data['name']
      address = data['address']
      category = data['category']
      distance = data['distance']
      website = data['website']

      sql = f'''
        INSERT INTO hospitals(name, address, category, distance, website)
        VALUES("{name}", "{address}", "{category}", "{distance}", "{website}")
      '''
      cursor.execute(sql)
      connection.commit()
      
      return {
        'status': 'success'
      }
    except KeyError:
      return{
        'status': 'fail',
        'message': 'missing fields'
      }, 404

@app.route('/api/hospitals', methods=['GET'])
def gethospitals():
  if request.method == 'GET':
    sql = '''
      SELECT name, address, category, distance, website FROM hospitals
      ORDER BY name ASC
    '''
    cursor.execute(sql)
    rows = cursor.fetchall()
    data = [
      {
        'name': hospitals[0],
        'address': hospitals[1],
        'category': hospitals[2],
        'distance': hospitals[3],
        'website': hospitals[4]
      } for hospitals in rows
    ]
    return{
      'status': 'success',
      'hospitals': data
    }

@app.route('/api/hospital/<id>', methods=['GET', 'PUT', 'DELETE'])
def hospital_id(id):
  id = int(id)

  if request.method == 'GET':
    sql = f'''
      SELECT name, address, category, distance, website from hospitals
      WHERE id = {id}
    '''

    cursor.execute(sql)
    row = cursor.fetchone()

    data = {
      'name': row[0],
      'address': row[1],
      'category': row[2],
      'distance': row[3],
      'website': row[4]
    }

    return {
      'status': 'success',
      'data': data
    }
  elif request.method == 'PUT':
    data = request.json

    for name, value in data.items():
      if type(value) is str:
        sql = f'''
          UPDATE hospitals
          SET "{name}" = "{value}"
          WHERE id = {id}
        '''
      elif type(value) is int:
        sql = f'''
        UPDATE hospitals
        SET "{name}" = {value}
        WHERE id = {id}
        '''

      cursor.execute(sql)
      connection.commit()

    return{
      'status': 'success'
    }
  elif request.method == 'DELETE':
    sql = f'''
      DELETE FROM hospitals
      WHERE id = {id}
    '''
    cursor.execute(sql)
    return{
      'status': 'success'
    }


# design a new route that is /api/hospital/longest, methods is get
# return only one hospital with the highest distance

@app.route('/api/hospital/longest', methods = ['GET'])
def longest_hospital():
  sql = '''
    SELECT * FROM hospitals
    ORDER BY distance DESC
    LIMIT 1
  '''
  cursor.execute(sql)
  row = cursor.fetchone()
  return{
    'status': 'success',
    'hospital': row
  }

app.run(host='0.0.0.0', port=81)


