from flask import Flask

def create_app( config_path='resource/config.cfg' ):
    print('create_app')
    # 플라스크 객체를 생성
    app = Flask(__name__)
    #=======================================================================
    # 환경 변수 로드 => 파일로 부터, 클래스로 정의된 환경변수 객체로부터
    app.config.from_pyfile( config_path, silent=True )
    print( app.config.items() )
    # 디비 로드 => 디비와 연결등등...
    # blueprint 생성 및 연결 작업 => 컨트롤러

    #=======================================================================
    # 플라스크 객체를 반환
    return app    