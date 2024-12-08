from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import literal_column
 
# 假设有如下的表结构
Base = declarative_base()
 
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
 
# 连接数据库
engine = create_engine('sqlite:///./he.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
 
# 创建一些示例数据
session.add_all([
    User(name='Alice', age=30),
    User(name='Bob', age=22),
])
session.commit()
 
# 创建一个虚拟列并指定别名
virtual_column = literal_column('\'dict\'').label('dict')
 
# 执行查询并将结果以字典形式返回
query = select([virtual_column, User.name, User.age]).with_column('dict', literal_column('1'))
result = session.execute(query).fetchall()
 
# 将结果转换为字典列表
results_dict = [dict(row) for row in result]
 
# 输出结果
print(results_dict)