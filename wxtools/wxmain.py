from flask import Flask
from flask import g #g对象可以使用before_request()和teardown_request(),即请求开始前和结束后
import sqlite3
import os


app = Flask(__name__)


DATABASE_INITFILE = "./schema.sql"
DATABASE = "./sql.db"
def connect_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = g.db = sqlite3.connect(DATABASE)
    return db
 
def init_db(): #使用数据库建模文件初始化数据库，在命令行中使用一次即可。
    print(".sql file path:{}".format(DATABASE_INITFILE))
    with app.app_context():
        db = connect_db()
        with app.open_resource(DATABASE_INITFILE, mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
 
@app.before_request
def before_request():
    g.db=connect_db()
 
@app.teardown_request
def close_db(exception):
    if hasattr(g, 'db'):
        g.db.close()