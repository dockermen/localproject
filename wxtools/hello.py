from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, MetaData, Table


from sqlalchemy import event
from flask import Flask,request
from flask_migrate import Migrate
import datetime,json

app = Flask(__name__)
# 步骤1：配置创建数据库参数
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./first.db" # 数据库存放位置
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "hello"

## 步骤2：实例化的数据库
db = SQLAlchemy(app)
metadata = MetaData()
migrate = Migrate(app, db)


# 步骤3：以db.Model为基类创建自己的ORM类
class VideoInfo(db.Model):
    # 步骤4 确定表名 __tablename__
    __tablename__ = "VideoInfo"
    # 步骤5：利用类属性创建表中字段
    id = db.Column(db.Integer, primary_key=True)  # 主键
    #title = db.Column(db.String(64), nullable=False)
    title = db.Column(db.String(64))
    url = db.Column(db.String(128))
    url_key = db.Column(db.String(64))
    password = db.Column(db.String(64))
    createtime = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    updatetime = db.Column(db.DateTime, default=datetime.datetime.now, comment='修改时间')
    visitor_num = db.Column(db.Integer,default=0,autoincrement=True)


def add_data(title,url,url_key,password):
    with app.app_context():
        s = VideoInfo(title=title,url=url,url_key=url_key,password=password)
        db.session.add(s)
        db.session.commit()
    return {"success":200}


def query_data(title):
    with app.app_context():
        alltblist = []
        
        queraw = VideoInfo.query.filter(VideoInfo.title.like("短剧%")).all()
        for i in queraw:
            alltb = {}
            alltb["id"] = i.id
            alltb["title"] = i.title
            alltb["url"] = i.url
            alltb["url_key"] = i.url_key
            alltb["password"] = i.password
            # alltb["createtime"] = i.createtime
            # alltb["updatetime"] = i.updatetime
            alltb["visitor_num"] = i.visitor_num
            alltblist.append(alltb)
        return alltblist
        
        
@app.route('/query/<title>', methods=['GET'])
def query(title):
    data = query_data(title)
    return data

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    add_data(data["title"],data["url"],data["url_key"],data["password"])
    return {"success":200}







if __name__ == '__main__':
    #app.run(host="0.0.0.0",debug=True)
    # 步骤6：利用db.create_all将ORM模型映射到数据库中
    # 注意：将模型映射到数据库中后，即使改变了模型的字段，也不会再重新映射修改表内容。
    with app.app_context(): # Create an :class:`~flask.ctx.AppContext`.
        db.create_all()
    #db.drop_all()
    # user = db.session.execute(db.text('SELECT * FROM VideoInfo'))
    # print(user.mappings().fetchall())