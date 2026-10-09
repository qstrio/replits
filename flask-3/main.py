from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from datetime import datetime
from hashlib import sha256
import os
app = Flask(__name__)

db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
salt = os.environ['SALT']
class User(db.Model):
  id = db.Column(db.Integer, primary_key =True)
  first_name = db.Column(db.String(100), nullable=False)
  last_name = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String(255), nullable=False)
  password = db.Column(db.String)
  date = db.Column(db.DateTime, nullable=False)
  jobs = db.relationship('Job', backref = 'user', cascade = 'all, delete', lazy = True)

class Job(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(150), nullable = False)
  exp = db.Column(db.Integer, nullable = False)
  company = db.Column(db.String(255), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  

@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route('/api/user/login', methods=['POST'])
def login():
  if request.method == 'POST':
    data = request.json

    try:
      email = data['email']
      password = data['password']

      user = User.query.filter_by(email=email).first()

      if not user:
        return{
          'status': 'fail',
          'message': 'The email or password is incorrect.'
        }, 400

      print('test')
      hash_password = sha256()
      hash_password.update(salt.encode())
      hash_password.update(password.encode())
  
      if user.password == hash_password.hexdigest():
        token = create_access_token(user.id)

        return{
          'status': 'success',
          'token': token
        }
      return {
        'status': 'fail',
        'message': 'The email or password is incorrect.'
      }, 400

    except KeyError:
      return {
        'status': 'fail',
        'message': 'Missing email or password.'
      }, 404


@app.route('/api/user/create', methods=['POST'])
def create_user():
  if request.method == 'POST':
    try:
      data = request.json
      first_name = data['first_name']
      last_name = data['last_name']
      email = data['email']
      password = data['password']
      date = datetime.now()

      hash_password = sha256()
      hash_password.update(salt.encode())
      hash_password.update(password.encode())
      
      user = User(
        first_name = first_name,
        last_name = last_name,
        email=email,
        password=hash_password.hexdigest(),
        date=date
      )

      db.session.add(user)
      db.session.commit()

      return{
        'status': 'success',
        'message': 'A new user has been created.'
      }, 201
    except KeyError:
      return{
        'status': 'failure',
        'message': 'Missing fields.'
      }, 404



@app.route('/api/user', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def user_handler():
  id = get_jwt_identity()
  user = User.query.get_or_404(id)

  if request.method == 'GET':
    jobs = user.jobs
    jobs_data = [
      {
        'title': job.title,
        'company': job.company,
        'experience': job.exp
      } for job in jobs
    ]
    data = {
      'first_name': user.first_name,
      'last_name': user.last_name,
      'email': user.email,
      'date': user.date,
      'jobs': jobs_data
    }

    return {
      'status': 'success',
      'user': data
    }
  elif request.method == 'PUT':
    data = request.json
    first_name = data.get('first_name', user.first_name)
    last_name = data.get('last_name', user.last_name)
    email = data.get('email', user.email)
    password = data.get('password', None)

    if password:
      hash_password = sha256()
      hash_password.update(salt.encode())
      hash_password.update(password.encode())
      user.password = hash_password.hexdigest()
      
    user.first_name = first_name
    user.last_name = last_name
    user.email = email

    db.session.commit()

    return {
      'status': 'success',
      'message': 'Updated successfully.'
    }


  elif request.method == 'DELETE':
    db.session.delete(user)
    db.session.commit()
    return {
      'status': 'success',
      'message': 'The user has been deleted.'
    }

@app.route('/api/job/create', methods = ["POST"])
@jwt_required()
def create_job():
  if request.method == 'POST':
    data = request.json
    user_id = get_jwt_identity()

    try:
      title = data['title']
      exp = data['exp']
      company = data['company']
      job = Job(
        title = title,
        exp = exp,
        company = company,
        user_id = user_id
      )
      db.session.add(job)
      db.session.commit()
      return {
        'status': 'success',
        'message': 'A job has been added to your profile'
      }, 201
    except KeyError: 
      return {
        'status': 'failure',
        'message': 'Missing fields'
      }, 404

@app.route('/api/job/<id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def job_handler(id):
  job = Job.query.get_or_404(int(id))
  user_id = get_jwt_identity()

  if user_id != job.user_id:
    return {
      'status': 'fail',
      'message': 'Access denied'
    }, 400
    
  if request.method == 'GET':
    user = User.query.get_or_404(job.user_id)
    data = {
      'title': job.title,
      'company': job.company,
      'experience': job.exp,
      'name': f'{user.first_name} {user.last_name}'
    }
    return{
      'status': 'success',
      'job': data
    }
  elif request.method == 'PUT':
    data = request.json
    title = data.get('title', job.title)
    exp = data.get('experience', job.exp)
    company = data.get('company', job.company)
    job.title = title
    job.exp = exp
    job.company = company
    db.session.commit()
    return {
      'status': 'success',
      'message': 'The job information has been updated'
    }
  elif request.method == 'DELETE':
    db.session.delete(job)
    db.session.commit()
    return{
      'status': 'success',
      'message': 'The job has been deleted'
    }

app.run(host='0.0.0.0', port=81)
