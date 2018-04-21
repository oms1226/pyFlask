from service.model import Base
from sqlalchemy import Column, Integer, String
from enum import unique

# 클래스가 테이블과 매핑된다.
class User(Base):
    # 테이블명
    __tablename__ = 'user'
    # 컬럼
    id          = Column(Integer,   primary_key=True)
    name        = Column(String(50),unique = True)
    password    = Column(String(50),unique = False)
    # 컬럼값 세팅
    def __init__(self, name, password):
        self.name = name
        self.password = password
    # 클래스가 가진 멤버의 값 출력( toString() )
    def __repr__(self):
        return "<User %s %s>" % (self.name, self.password)