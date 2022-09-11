from typing import Tuple
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 单例模式
app = None
db = None

def get_app(name: str) -> Tuple[Flask, SQLAlchemy]:
    global app, db
    if app is None or db is None:
        app = Flask(name)
        mysql_host = os.getenv('MYSQL_HOST')
        if mysql_host:
            app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:camrsti@{mysql_host}:3306/camrstidb'
        else:
            app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:camrsti@localhost:3306/camrstidb'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
        db = SQLAlchemy(app)
    return app, db
