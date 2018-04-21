# 기본 디비 연결 모듈을 wrapping 하는 모듈 사용하여
# 가상환경 venv 상에서 설치
## pip install sqlalchemy
###D:\py_project>cd venv
###D:\py_project\venv>cd Scripts
###D:\py_project\venv\Scripts>activate.bat
###(venv) D:\py_project\venv\Scripts>pip install sqlalchemy
# 고급 쿼리 및 ORM 처리로 디비 작업 수행
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

class DBManager:
    # 멤버 변수
    __engine = None
    __session = None

    # static 함수 활용
    @staticmethod
    def init( db_url, db_log_flag=False ):
        # 엔진 초기화
        DBManager.__engine = create_engine(db_url, echo=db_log_flag)# DBManager.__engine 또한 static 변수처럼 사용된다고 이해하면 된다.
        # 세션 초기화
        DBManager.__session = scoped_session( sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=DBManager.__engine
        ) )
        global dao
        dao = DBManager.__session
        print('초기화')
    
    @staticmethod
    def init_table():
        print('테이블이 없으면 생성')            
        # 회원 테이블 user 부재 시 생성
        # 관련 테이블과 연결된 클래스 import
        from service.model import user
        from service.model import Base

        #생성
        Base.metadata.create_all( bind = DBManager.__engine)


# 디비 세션을 가르킨다.
dao = None