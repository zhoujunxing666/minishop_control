from flask import Flask, request, session, redirect, url_for, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import hashlib

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/mydatabase'
app.config['SECRET_KEY'] = 'mysecretkey'  # 更好的安全性需要使用更复杂的密钥
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    store_name = db.Column(db.String(120), nullable=False)
    store_address = db.Column(db.String(120), nullable=False)
    registration_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def index():#FixIt
    return 'Hello, World!'


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 从表单中获取数据
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        phone = request.form['phone']
        store_name = request.form['store_name']
        store_address = request.form['store_address']

        # 检查用户名和电子邮件是否唯一
        if User.query.filter_by(username=username).first():
            return '用户名已存在'
        if User.query.filter_by(email=email).first():
            return '电子邮件已存在'

        # 创建新用户
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        new_user = User(username=username, password=hashed_password, email=email,
                        phone=phone, store_name=store_name, store_address=store_address)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    # GET 请求，显示注册表单
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 从表单中获取数据
        username = request.form['username']
        password = request.form['password']

        # 根据用户名查询用户
        user = User.query.filter_by(username=username).first()

        # 检查用户名和密码是否正确
        if user and user.password == hashlib.sha256(password.encode()).hexdigest():
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect(url_for('index'))
        else:
            return '用户名或密码错误'

    # GET 请求，显示登录表单
    return render_template('login.html')

# 修改邮箱的路由
@app.route('/users/<int:user_id>/email', methods=['PUT'])
def change_email(user_id):
    # 获取请求中的新邮箱地址
    new_email = request.json.get('email')
    if not new_email:
        return jsonify({'error': 'Missing email'}), 400
    
    # 根据用户 ID 获取用户信息
    user = users.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    # 更新用户邮箱
    user['email'] = new_email
    
    # 返回更新后的用户信息
    return jsonify(user), 200

# 修改手机号码的路由
@app.route('/users/<int:user_id>/phone', methods=['PUT'])
def change_phone(user_id):
    # 获取请求中的新手机号码
    new_phone = request.json.get('phone')
    if not new_phone:
        return jsonify({'error': 'Missing phone'}), 400
    
    # 根据用户 ID 获取用户信息
    user = users.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    # 更新用户手机号码
    user['phone'] = new_phone
    
    # 返回更新后的用户信息
    return jsonify(user), 200

# 修改密码的路由
@app.route('/users/<int:user_id>/password', methods=['PUT'])
def change_password(user_id):
    # 获取请求中的新密码
    new_password = request.json.get('password')
    if not new_password:
        return jsonify({'error': 'Missing password'}), 400
    
    # 根据用户 ID 获取用户信息
    user = users.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    # 更新用户密码
    user['password'] = new_password
    
    # 返回更新后的用户信息
    return jsonify(user), 200





#if __name__ == '__main__':
    app.run(debug=True)
