"""
用户模型与模拟数据库相关操作。
"""
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

# 模拟数据库
users = {}

# 用户模型函数


def create_user(email, password):
    """
    创建新用户并保存到模拟数据库。
    :param email: 用户邮箱
    :param password: 明文密码
    :return: 用户字典对象
    """
    hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
    user = {
        'email': email,
        'password': hashed_pw,
        'role': 'user',
        'permissions': ['view_profile']
    }
    users[email] = user
    return user


def get_user(email):
    """
    根据邮箱获取用户信息。
    :param email: 用户邮箱
    :return: 用户字典对象或 None
    """
    return users.get(email)
