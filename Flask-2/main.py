from flask import Flask, request
import sqlite3

connection = sqlite3.connect('store.db', check_same_thread=False)
cursor = connection.cursor()

sql = '''
  CREATE TABLE products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name CHAR(255) NOT NULL,
    brand CHAR(125) NOT NULL,
    category CHAR(175) NOT NULL, 
    price INT NOT NULL
  )
'''


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route('/api/products', methods=['GET', 'POST'])
def products():
  if request.method == 'GET':
    sql = '''
    SELECT name, brand, category, price FROM products
    ORDER BY brand ASC
    '''
    cursor.execute(sql)
    rows = cursor.fetchall()
    data = [
      {
        'name': product[0],
        'brand': product[1],
        'category': product[2],
        'price': product[3]
      } for product in rows 
    ]
    return{
      'status': 'success',
      'products': data
    }
  elif request.method == 'POST':
    data = request.json
    try:
      name = data['name']
      brand = data['brand']
      category = data['category']
      price = data['price']
  
      sql = f'''
        INSERT INTO products(name, brand, category, price)
        VALUES("{name}", "{brand}", "{category}", {price})
      '''
      cursor.execute(sql)
      connection.commit()
      return {
        'status': 'success'
      }
    except:
      return {
        'status': 'fail',
        'message': 'Missing Fields'
      }, 404

@app.route('/api/product/<id>', methods=['GET', 'PUT', 'DELETE' ])
def product(id):
  id = int(id)

  if request.method == 'GET':
    sql = f'''
      SELECT name, brand, category, price from products
      WHERE id = {id}
    '''
  
    cursor.execute(sql)
    row = cursor.fetchone()
  
    data = {
      'name': row[0],
      'brand': row[1],
      'category': row[2],
      'price': row[3]
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
        UPDATE products
        SET "{name}" = "{value}"
        WHERE id = {id}
        '''
      elif type(value) is int:
        sql = f'''
          UPDATE products
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
    DELETE FROM products
    WHERE id = {id}
    '''
    cursor.execute(sql)

    return {
      'status': 'success'
    }


app.run(host='0.0.0.0', port=81)
