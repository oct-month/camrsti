from typing import Tuple, Optional
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import DATABASE_URI

# 单例模式
app = None
db = None

def get_app(name: Optional[str]=None) -> Tuple[Flask, SQLAlchemy]:
    global app, db
    if app is None or db is None:
        if name is None:
            raise RuntimeError('db initial fail')
        app = Flask(name)
        app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
        app.config['SQLALCHEMY_ECHO'] = True
        db = SQLAlchemy(app)
    return app, db
