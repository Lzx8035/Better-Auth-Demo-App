"""
用户相关接口路由。
"""
from flask import Blueprint, request, jsonify
from utils.jwt import decode_token
from models import User

user_bp = Blueprint('user', __name__)


@user_bp.route('/me', methods=['GET', 'OPTIONS'])
def get_current_user():
    """
    获取当前用户信息，需携带有效 JWT。
    :return: 用户信息或错误信息 JSON
    """
    if request.method == 'OPTIONS':
        return '', 200

    auth_header = request.headers.get('Authorization')

    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({'error': 'Missing token'}), 401

    token = auth_header.split(' ')[1]
    payload = decode_token(token)

    if not payload:
        return jsonify({'error': 'Invalid or expired token'}), 401

    return jsonify({'user': payload})


# 后续更改为管理员接口
@user_bp.route('/users', methods=['GET', 'OPTIONS'])
def get_all_users():
    """
    获取所有用户信息，需携带有效 JWT。
    :return: 用户列表或错误信息 JSON
    """
    if request.method == 'OPTIONS':
        return '', 200

    auth_header = request.headers.get('Authorization')

    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({'error': 'Missing token'}), 401

    token = auth_header.split(' ')[1]
    payload = decode_token(token)

    if not payload:
        return jsonify({'error': 'Invalid or expired token'}), 401

    try:
        # 获取所有用户，排除密码字段
        users = User.query.all()
        users_data = []

        for user in users:
            users_data.append({
                'id': user.id,
                'email': user.email,
                'role': user.role,
                'permissions': user.permissions
            })

        return jsonify({
            'users': users_data,
            'total': len(users_data)
        }), 200

    except Exception as e:
        return jsonify({'error': 'Failed to fetch users', 'message': str(e)}), 500
