from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

users_db = {}

@app.route('/api/users/register', methods=['POST'])
def register_user():
    data = request.get_json()
    email = data.get('email')
    if not email or email in users_db:
        return jsonify({'error': 'Email already exists or invalid'}), 400
    password = data.get('password')
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
    users_db[email] = {'email': email, 'password': hashed_password}
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/api/users/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = users_db.get(email)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({'error': 'Invalid credentials'}), 401
    token = jwt.encode({'email': email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, app.config['SECRET_KEY'], algorithm='HS256')
    return jsonify({'token': token})

if __name__ == '__main__':
    app.run(debug=True)
