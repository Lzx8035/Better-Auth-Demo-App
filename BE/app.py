"""
应用主入口，负责注册蓝图和启动 Flask 服务。
"""
from routes.user import user_bp
from routes.auth import auth_bp
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from models import db

app = Flask(__name__)
app.config.from_pyfile('config.py')

db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()

# 允许跨域
CORS(app)

# 注册蓝图
app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(user_bp, url_prefix='/api')


@app.route('/')
def hello():
    """
    健康检查接口，返回服务运行状态。
    :return: JSON，包含服务状态和欢迎信息
    """
    return jsonify({
        'message': 'Flask 服务已启动',
        'status': 'success'
    })


if __name__ == '__main__':
    app.run(debug=True)
