"""
应用主入口，负责注册蓝图和启动 Flask 服务。
"""
from routes.user import user_bp
from routes.auth import auth_bp
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config.from_pyfile('config.py')  # 加载配置

CORS(app)  # 允许跨域

# 注册蓝图

app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(user_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
