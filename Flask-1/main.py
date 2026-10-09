from flask import Flask, request

app = Flask(__name__)

students = [
  'Sarah',
  'James', 
  'David',
  'Daniel'
]


@app.route('/')
def index():
    return 'Hello from Flask!'


@app.route('/api/student', methods=['GET', 'POST'])
def get_students():
  if request.method == 'GET':
    return{
      'status' : 'success',
      'data' : students
    }
  elif request.method == 'POST':
    data = request.json
    name = data['name']
    students.append(name)

    return {
      'status': 'success',
      'message': 'The student has been added.'
      
    }

@app.route('/api/student/<index>', methods=['PUT', 'DELETE', 'GET'])
def get_student(index):
  index = int(index)
  if request.method == 'PUT':
    try:
      name = request.json['name']
      students[index] = name
      return{
        'status': 'success'
      }
    except:
      return{
        'status': 'fail',
        'message': "Invalid Index Number"
      }, 400
  elif request.method == 'DELETE':
    try:
      students.pop(index)
      return {
        'status': 'success'
      }
    except:
      return {
        'status': 'fail',
        'message': 'Invalid Index Number'
      }, 400
  elif request.method == 'GET':
    try:
      name = students[index]
      return {
        'status': 'success',
        'name': name
        
      }
    except:
      return {
        'status': 'fail',
        'message': 'Invalid Index Number'
      }, 400
    
    
app.run(host='0.0.0.0', port=81)

