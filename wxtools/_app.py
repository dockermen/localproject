from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate


app = Flask(__name__)
# 步骤1：配置创建数据库参数
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./first.db" # 数据库存放位置
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "hello"

## 步骤2：实例化的数据库
db = SQLAlchemy(app)

migrate = Migrate(app, db)


# 步骤3：以db.Model为基类创建自己的ORM类
class Student(db.Model):
    # 步骤4 确定表名 __tablename__
    __tablename__ = "student"
    # 步骤5：利用类属性创建表中字段
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(64), nullable=False)  # 学生姓名 nullable能否为空
    phone = db.Column(db.String(11))  # 手机号 可以为空
    nikname = db.Column(db.String(64))

# def update_sql():
#     db.cr


# if __name__ == '__main__':
#     # 步骤6：利用db.create_all将ORM模型映射到数据库中
#     # 注意：将模型映射到数据库中后，即使改变了模型的字段，也不会再重新映射修改表内容。
#     with app.app_context():  # Create an :class:`~flask.ctx.AppContext`.
#         #db.create_all()
#         db.Table.append_column(column = db.Column(db.String(64)))
#         #db.drop_all()
