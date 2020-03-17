from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from sqlalchemy import Column, DateTime, String, Text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager
import traceback


class SQLAlchemy(_SQLAlchemy):
    """
    设置自动提交事务，发生异常则回滚
    @contextmanager作用是把任意对象变为上下文对象，并支持with语句
    """
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            traceback.print_exc()


app = FlaskAPI(__name__)
# mysql+pymysql://username:password@hostname/database?charset
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://my_rds:8EbSJxZa_qFgsQ2@helloworld.mysql.rds.aliyuncs.com:3306/production'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(320), unique=True)
    password = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(320), unique=True)
    password = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return '<Student %r>' % self.name


if __name__ == '__main__':
    # db.create_all() # 创建表
    # db.drop_all()  # 删除表

    # 插入数据
    # stu1 = Student(name='lucy', email='2@1234.com', password='123')
    # stu2 = Student(name='tom', email='3@1234.com', password='123')
    # with db.auto_commit():
    #     db.session.add(stu1)
    #     db.session.add(stu2)
    """
    filter_by精确查询 参数里面为=且字段不用表名引出
    filter模糊查询 参数里面为==
    first()返回查询到的第一个对象 , all()返回查询到的所有对象 
    """
    # 查询数据
    # stu = Student.query.filter_by(email='3@1234.com').first()
    # print(type(stu), stu)   # <class '__main__.Student'>
    # print(stu.name, stu.email, stu.password)

    # stu_query = Student.query.filter(Student.email == '3@1234.com')
    # print(f'type of stu_query:{type(stu_query)}')  # <class 'flask_sqlalchemy.BaseQuery'>
    # print(stu_query.first().name, stu_query.first().email, stu_query.first().password)

    # 更新数据
    # with db.auto_commit():
    #     stu_query.update({Student.password: '456'})
    # stu_query.first().password = '456'

    # 删除数据
    # stu = Student.query.filter_by(email='3@1234.com').first()
    # with db.auto_commit():
    #     db.session.delete(stu)

    pass
