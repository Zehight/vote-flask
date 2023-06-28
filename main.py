# 创建一个Flask应用,解决跨域
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*', methods=['GET', 'POST', 'OPTIONS'])

# 加入基本目录
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# 导入依赖（snowflake）
from datetime import datetime
from snowflake import Snowflake

snowflake = Snowflake(0, 0, 0, datetime(2020, 1, 1))

# 导入环境变量
from env import Config

app.config.from_object(Config)

# 导入数据库
from models import db, connect_db

# 数据库初始化.
connect_db(app)

# 导入蓝图
from Controller.project import project
from Controller.health import health
from Controller.file import file
from Controller.role import role
from Controller.round import round
from Controller.group import group

app.register_blueprint(project)
app.register_blueprint(health)
app.register_blueprint(file)
app.register_blueprint(role)
app.register_blueprint(round)
app.register_blueprint(group)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
