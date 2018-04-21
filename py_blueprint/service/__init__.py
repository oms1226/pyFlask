from flask import Flask

def create_app( config_path='resource/config.cfg' ):
    print('create_app')
    # 플라스크 객체를 생성
    app = Flask(__name__)
    #=======================================================================
    # 환경 변수 로드 => 파일로 부터, 클래스로 정의된 환경변수 객체로부터
    # 파일로 부터 로드, silent=True 는 습관적으로 쓴다고 한다. 정확한 이유는 모르겠다.
    app.config.from_pyfile( config_path, silent=True )
    # 객체로 부터 로드
    from service.app_config import WebConfig
    app.config.from_object( WebConfig )
    #print( app.config.items() )#출력결과:#dict_items([('DEBUG', False), ('TESTING', False), ('PROPAGATE_EXCEPTIONS', None), ('PRESERVE_CONTEXT_ON_EXCEPTION', None), ('SECRET_KEY', None), ('PERMANENT_SESSION_LIFETIME', datetime.timedelta(31)), ('USE_X_SENDFILE', False), ('LOGGER_NAME', 'service'), ('LOGGER_HANDLER_POLICY', 'always'), ('SERVER_NAME', None), ('APPLICATION_ROOT', None), ('SESSION_COOKIE_NAME', 'session'), ('SESSION_COOKIE_DOMAIN', None), ('SESSION_COOKIE_PATH', None), ('SESSION_COOKIE_HTTPONLY', True), ('SESSION_COOKIE_SECURE', False), ('SESSION_REFRESH_EACH_REQUEST', True), ('MAX_CONTENT_LENGTH', None), ('SEND_FILE_MAX_AGE_DEFAULT', datetime.timedelta(0, 43200)), ('TRAP_BAD_REQUEST_ERRORS', False), ('TRAP_HTTP_EXCEPTIONS', False), ('EXPLAIN_TEMPLATE_LOADING', False), ('PREFERRED_URL_SCHEME', 'http'), ('JSON_AS_ASCII', True), ('JSON_SORT_KEYS', True), ('JSONIFY_PRETTYPRINT_REGULAR', True), ('JSONIFY_MIMETYPE', 'application/json'), ('TEMPLATES_AUTO_RELOAD', None), ('TEST_MODE', True), ('TEST_URL', '127.0.0.1')])
    #print( app.config.keys() )
    #print( app.config.values() )
    #print( 'DB_URL:', app.config['DB_URL'])
    # 디비 로드 => 디비와 연결등등...
    print( 'DB_URL:', app.config['DB_URL'])
    # 연결 문자열
    db_url = "mysql+pymysql://%s:%s@%s/%s?charset=%s" % (
        app.config['DB_USER'],
        app.config['DB_PASSWORD'],
        app.config['DB_URL'],
        app.config['DB_DATABASE'],
        app.config['DB_CHARSET']
    )
    print ( "연결문자열:", db_url )#mysql+pymysql://root:0000@localhost/pythondb?charset=utf8
    from service.app_database import DBManager
    # eval()은 원래 의도된 타입으로 적용되어 반환됨 'True' -> True
    DBManager.init(db_url, eval(app.config['DB_LOG_FLAG']) )

    # blueprint 생성 및 연결 작업 => 컨트롤러

    #=======================================================================
    # 플라스크 객체를 반환
    return app