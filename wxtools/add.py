from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from hello import VideoInfo
app = Flask(__name__)
# 步骤1：配置创建数据库参数
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./first.db" # 数据库存放位置
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "hello"

## 步骤2：实例化的数据库
db = SQLAlchemy(app)


# 步骤3：以db.Model为基类创建自己的ORM类
class Student(db.Model):
    # 步骤4 确定表名 __tablename__
    __tablename__ = "student"
    # 步骤5：利用类属性创建表中字段
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(64))  # 学生姓名 nullable能否为空
    test = db.Column(db.String(64))  # 学生姓名 nullable能否为空
    phone = db.Column(db.String(11))  # 手机号 可以为空


# 增
def add_data():
    #s = Student(name="major",test="testa",phone="1777777777")
    s = VideoInfo(title="短剧",url="http://quick.cn",url_key="123456",password="123456")
    # 加入session
    db.session.add(s)
    # session提交
    db.session.commit()

# 删
def del_data():
    user = Student.query.first()
    # 加入session
    db.session.delete(user)
    # session提交
    db.session.commit()

# 改

# 查


if __name__ == '__main__':
    # 步骤6：利用db.create_all将ORM模型映射到数据库中
    with app.app_context():  # Create an :class:`~flask.ctx.AppContext`.
        # 建立表
        #db.create_all()
        # db.drop_all() # 删除所有表
        # 添加数据
        add_data()
        #删除数据
        #del_data()

