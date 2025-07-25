"""
配置文件：包含密钥和 JWT 相关设置。
"""
import os

SECRET_KEY = 'k1Qw2e3r4t5y6u7i8o9p0a1s2d3f4g5h6'  # 用于 JWT
JWT_EXPIRE_SECONDS = 3600  # token 有效期：1小时

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'ba.db')}"

SQLALCHEMY_DATABASE_URI = DATABASE_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False
