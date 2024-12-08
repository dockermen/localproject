from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'
db = SQLAlchemy(app)
 
# 定义模型
class MyModel(db.Model):
    id = Column(Integer, primary_key=True)
    # 其他字段...
    visit_count = Column(Integer, default=0)
 
# 定义信号
from sqlalchemy import event
 
@event.listens_for(MyModel, 'init')
def increment_visit_count(mapper, connection, instance):
    instance.visit_count += 1
 
# 使用模型
if __name__ == "__main__":
    with app.app_context():
        #db.create_all()
    
        # 创建一个模型实例
        model_instance = MyModel()
        # db.session.add(model_instance)
        # db.session.commit()
        #increment_visit_count(model_instance)
        # 访问模型实例，visit_count会自动增加
        print(model_instance.visit_count)  # 输出 1
        print(model_instance.visit_count)  # 输出 2