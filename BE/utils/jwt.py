import jwt
import datetime
from config import SECRET_KEY, JWT_EXPIRE_SECONDS


def create_token(user):
    payload = {
        'email': user['email'],
        'role': user['role'],
        'permissions': user['permissions'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=JWT_EXPIRE_SECONDS)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')


def decode_token(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
