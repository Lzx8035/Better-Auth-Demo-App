"""
JWT 工具函数。
"""
import datetime
import jwt
from config import SECRET_KEY, JWT_EXPIRE_SECONDS


def create_token(user):
    """
    创建 JWT token。
    """
    payload = {
        'id': user.id,
        'email': user.email,
        'role': user.role,
        'permissions': user.permissions,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=JWT_EXPIRE_SECONDS)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')


def decode_token(token):
    """
    解码 JWT token。
    """
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
