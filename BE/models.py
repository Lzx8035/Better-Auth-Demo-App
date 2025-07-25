"""
数据库模型定义。
"""
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()


class User(db.Model):
    """
    用户模型。
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), default='user')
    permissions = db.Column(db.PickleType, default=lambda: ['view_profile'])

    def check_password(self, password_plaintext):
        """
        检查密码是否正确。
        """
        return bcrypt.check_password_hash(self.password, password_plaintext)

    @classmethod
    def create(cls, email, password):
        """
        创建新用户。
        """
        hashed = bcrypt.generate_password_hash(password).decode('utf-8')
        return cls(email=email, password=hashed)
