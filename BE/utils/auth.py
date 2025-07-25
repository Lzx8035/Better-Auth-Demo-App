"""
认证相关接口路由。
"""
from flask import Blueprint, request, jsonify
from models import create_user, get_user, bcrypt
from utils.jwt import create_token

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    """
    用户注册接口，创建新用户并返回 token。
    :return: 注册结果 JSON
    """
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if get_user(email):
        return jsonify({'error': 'User already exists'}), 400

    user = create_user(email, password)
    token = create_token(user)
    return jsonify({'accessToken': token,
                    'user': {k: v for k, v in user.items() if k != 'password'}})


@auth_bp.route('/login', methods=['POST'])
def login():
    """
    用户登录接口，校验凭证并返回 token。
    :return: 登录结果 JSON
    """
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = get_user(email)
    if not user or not bcrypt.check_password_hash(user['password'], password):
        return jsonify({'error': 'Invalid credentials'}), 401

    token = create_token(user)
    return jsonify({'accessToken': token,
                    'user': {k: v for k, v in user.items() if k != 'password'}})
