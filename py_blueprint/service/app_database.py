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
        DBManager.__engine = create_engine(db_url, echo=db_log_flag)
        # 세션 초기화

        print('초기화')
    
    @staticmethod
    def init_table():
        print('테이블이 없으면 생성')    

