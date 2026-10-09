from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, JWTManager
from hashlib import sha256
from datetime import timedelta, datetime
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'
app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=7)
db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
salt = os.environ['SALT']

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String, unique=True, nullable=False)
  password = db.Column(db.String, nullable=False)
  name = db.Column(db.String(125))
  role = db.Column(db.String(20), nullable=False, default='user')
  birth = db.Column(db.DateTime)
  registration = db.Column(db.DateTime, nullable=False)
  active = db.Column(db.Boolean, nullable=False, default=True)
  country = db.Column(db.String(175))
  posts = db.relationship('Posts', backref='user', lazy=True)
  comments = db.relationship('Comments', backref='user')

class Category(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(125), nullable=False, unique=True)
  posts_id = db.relationship('Posts', backref='category', lazy=True)

class Posts(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  post_name = db.Column(db.String(200), nullable=False)
  post_content = db.Column(db.String(65000), nullable=False)
  post_date = db.Column(db.DateTime, nullable=False)
  views = db.Column(db.Integer, nullable=False, default=0)
  likes = db.Column(db.Integer, nullable=False, default=0)
  dislikes = db.Column(db.Integer, nullable=False,default=0)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
  comments = db.relationship('Comments', backref='posts')

class Comments(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  comment_content = db.Column(db.String(50000), nullable=False)
  comment_date = db.Column(db.DateTime, nullable=False)
  post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

@app.route('/')
def index():
  print(request.args)
  return 'Hello from Flask!'

@app.route('/api/v1/user/register', methods=['POST'])
def create_user():
  if request.method == 'POST':
    data = request.json

    try:
      email = data['email']
      password = data['password']
      name = data['name']
      birth =  datetime.strptime(data['birth'], '%Y-%m-%d')
      country = data['country']

      hash_password = sha256()
      hash_password.update(salt.encode())
      hash_password.update(password.encode())

      user = User(
        email=email,
        password=hash_password.hexdigest(),
        name=name,
        registration=datetime.now(),
        birth=birth,
        country=country
      )

      db.session.add(user)
      db.session.commit()

      return {
        'status': 'success',
        'message': f'{name} has registered a new account!'
      }, 201
    except KeyError:
      return {
        'status': 'fail',
        'message': 'Missing fields'
      }, 404

@app.route('/api/v1/user/login', methods=['POST'])
def login():
  if request.method == 'POST':
    data = request.json

    try:
      email = data['email']
      password = data['password']

      user = User.query.filter_by(email=email).first()

      if not user:
        return {
          'status': 'fail',
          'message': 'Invalid email or password'
        }, 400

      hash_password = sha256()
      hash_password.update(salt.encode())
      hash_password.update(password.encode())

      if user.password == hash_password.hexdigest():
        token = create_access_token(user.id)

        return {
          'status': 'success',
          'token': token
        }
        
      return {
          'status': 'fail',
          'message': 'Invalid email or password'
        }, 400

    except KeyError:
      return {
          'status': 'fail',
          'message': 'Missing email or password'
        }, 400

@app.route('/api/v1/user', methods=['GET', 'PUT'])
@jwt_required()
def user():
  user_id = get_jwt_identity()
  user = User.query.get_or_404(user_id)

  if not user:
    return {
      'status': 'fail',
      'message': 'Invalid user'
    }, 404

  if request.method == 'GET':
    user_info = {
      'email': user.email,
      'name': user.name,
      'birth': user.birth,
      'registration': user.registration,
      'country': user.country
    }

    return {
      'status': 'success',
      'user': user_info
    }
  elif request.method == 'PUT':
    data = request.json
    name = data.get('name', user.name)
    birth = data.get('birth', None)
    if birth:
      birth = datetime.strptime(birth, '%Y-%m-%d')
    else:
      birth = user.birth
    country = data.get('country', user.country)

    user.name = name
    user.birth = birth
    user.country = country

    db.session.commit()

    return {
      'status': 'success',
      'message': 'The user has been updated'
    }

@app.route('/api/v1/user/<id>/posts', methods=['GET'])
def get_user_post(id):
  if request.method == 'GET':
    user = User.query.get_or_404(int(id))
    posts = user.posts

    posts_data = [
      {
        'post_name': post.post_name,
        'post_content': post.post_content,
        'post_date': post.post_date,
      } for post in posts
    ]

    return {
      'status': 'success',
      'posts': posts_data
    }

@app.route('/api/v1/user/<id>/comments', methods=['GET'])
def get_user_comments(id):
  if request.method == 'GET':
    user = User.query.get_or_404(int(id))
    comments = user.comments

    comments_data = [
      {
        'comment_content': comment.comment_content,
        'comment_date': comment.comment_date
      } for comment in comments
    ]

    return {
      'status': 'success',
      'comments': comments_data
    }

@app.route('/api/v1/category/create', methods=['POST'])
@jwt_required()
def create_category():
  if request.method == 'POST':
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)

    if user.role != 'admin':
      return {
        'status': 'fail',
        'message': 'Access denied'
      }, 400

    data = request.json
    name = data.get('name', None)

    if not name:
      return {
        'status': 'fail',
        'message': 'Missing category name'
      }, 404

    category = Category(name=name)
    db.session.add(category)
    db.session.commit()

    return {
      'status': 'success',
      'message': f'The category {name} has been created'
    }, 201

@app.route('/api/v1/posts/create', methods=['POST'])
@jwt_required()
def create_post():
  if request.method == 'POST':
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    data = request.json

    try:
      post_name = data['post_name']
      post_content = data['post_content']
      category_id = data['category_id']

      post = Posts(
        post_name=post_name,
        post_content=post_content,
        post_date = datetime.now(),
        views=0,
        likes=0,
        dislikes=0,
        user_id=user_id,
        category_id=category_id
      )

      db.session.add(post)
      db.session.commit()

      return {
        'status': 'success',
        'message': 'The post has been created'
      }, 201
    except KeyError:
      return {
        'status': 'fail',
        'message': 'Missing values'
      }
    
@app.route('/api/v1/comments/create', methods=['POST'])
@jwt_required()
def create_comment():
  if request.method == 'POST':
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    data = request.json

    try:
      comment_content = data['comment_content']
      post_id = data['post_id']

      comment = Comments(
        comment_content=comment_content,
        comment_date=datetime.now(),
        post_id=post_id,
        user_id=user_id
      )

      db.session.add(comment)
      db.session.commit()

      return {
        'status': 'success',
        'message': 'You had made an comment'
      }
    except KeyError:
      return {
        'status': 'fail',
        'message': 'Missing values'
      }

@app.route('/api/v1/posts', methods=['GET'])
def get_all_posts():
  if request.method == 'GET':
    page = request.args.get('page', 1)
    category = request.args.get('category', None)

    if category:
      category = Category.query.filter_by(name=category).first()
      posts = Posts.query.filter_by(category_id=category.id)
    else:
      posts = Posts.query.filter_by()

    posts = posts.order_by(Posts.post_date.desc()).limit(10).offset(10 * (page - 1)).all()

    posts_data = [
      {
        'post_name': post.post_name,
        'post_date': post.post_date,
        'views': post.views
      } for post in posts
    ]

    return {
      'status': 'success',
      'posts': posts_data
    }

@app.route('/api/v1/posts/<id>', methods=['GET'])
def get_post(id):
  if request.method == 'GET':
    id = int(id)
    post = Posts.query.get_or_404(id)
    user = User.query.get_or_404(post.user_id)
    post_info = {
      'post_name': post.post_name,
      'post_content': post.post_content,
      'post_date': post.post_date,
      'views': post.views,
      'likes': post.likes,
      'dislikes': post.dislikes,
      'author': user.name,
    }

    return {
      'status': 'success',
      'post': post_info
    }

@app.route('/api/v1/posts/<id>', methods=['PUT', 'DELETE'])
@jwt_required()
def post_handler(id):
  id = int(id)
  post = Posts.query.get_or_404(id)
  user_id = get_jwt_identity()
  user = User.query.get_or_404(user_id)
  
  if post.user_id != user_id:
    return {
      'status': 'fail',
      'message': 'Access denied'
    }, 400
  
  if request.method == 'PUT':
    data = request.json
    post_name = data.get('post_name', post.post_name)
    post_content = data.get('post_content', post.post_content)

    post.post_name = post_name
    post.post_content = post_content

    db.session.commit()

    return {
      'status': 'success',
      'message': 'The post has been updated'
    }
  elif request.method == 'DELETE':
    db.session.delete(post)
    db.session.commit()
    return {
      'status': 'success',
      'message': 'The post hass been deleted'
    }
  
@app.route('/api/v1/comments/<id>', methods=['GET'])
def get_comments(id):
  if request.method == 'GET':
    id = int(id)
    post = Posts.query.get_or_404(id)
    page = int(request.args.get('page', 1))
    comments = Comments.query.filter_by(post_id=id).order_by(Comments.comment_date).limit(20).offset(20 * (page - 1)).all()

    output = []

    for comment in comments:
      user = User.query.filter_by(id=comment.user_id).first()
      data = {
        'name': user.name if user else 'Deleted User',
        'comment_content': comment.comment_content,
        'comment_date': comment.comment_date
      }

      output.append(data)

    return {
      'status': 'success',
      'comments': output
    }

@app.route('/api/v1/comments/<id>', methods=['PUT', 'DELETE'])
@jwt_required()
def comment_handler(id):
  comment = Comments.query.get_or_404(int(id))
  user_id = get_jwt_identity()
  user = User.query.get_or_404(user_id)

  if comment.user_id != user_id:
    return {
      'status': 'fail',
      'message': 'Access denied'
    }, 400

  if request.method == 'PUT':
    data = request.json
    comment_content = data.get('comment_content', comment.comment_content)
    comment.comment_content = comment_content
    db.session.commit()
    return {
      'status': 'success',
      'message': 'The comment has been updated'
    }
  elif request.method == 'DELETE':
    db.session.delete(comment)
    db.session.commit()
    return {
      'status': 'success',
      'message': 'The comment has been deleted'
    }

app.run(host='0.0.0.0', port=81)
