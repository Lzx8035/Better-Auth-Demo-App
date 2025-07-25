"""
用户相关接口路由。
"""
from flask import Blueprint, request, jsonify
from utils.jwt import decode_token

user_bp = Blueprint('user', __name__)


@user_bp.route('/me', methods=['GET'])
def get_current_user():
    """
    获取当前用户信息，需携带有效 JWT。
    :return: 用户信息或错误信息 JSON
    """
    auth_header = request.headers.get('Authorization')

    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({'error': 'Missing token'}), 401

    token = auth_header.split(' ')[1]
    payload = decode_token(token)

    if not payload:
        return jsonify({'error': 'Invalid or expired token'}), 401

    return jsonify({'user': payload})
