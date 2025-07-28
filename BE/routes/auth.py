"""
认证相关接口路由。
"""
from models import User, db
from flask import Blueprint, request, jsonify
from utils.jwt import create_token

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST', 'OPTIONS'])
def register():
    """
    用户注册接口，创建新用户。
    """
    if request.method == 'OPTIONS':
        return '', 200

    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'User already exists'}), 400

    new_user = User.create(email, password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully', 'user': serialize_user(new_user)})


@auth_bp.route('/login', methods=['POST', 'OPTIONS'])
def login():
    """
    用户登录接口，校验凭证并返回 token。
    """
    if request.method == 'OPTIONS':
        return '', 200

    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({'error': 'Invalid credentials'}), 401

    token = create_token(user)
    return jsonify({'accessToken': token, 'user': serialize_user(user)})


def serialize_user(user):
    """
    序列化用户数据。
    """
    return {
        'id': user.id,
        'email': user.email,
        'role': user.role,
        'permissions': user.permissions
    }
