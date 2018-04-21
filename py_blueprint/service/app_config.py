'''
환경변수를 담고 있는 클래스
해당 클래스를 등록하면 객체로 올려서 환경변수(맴버변수)를 로드한다
'''
class WebConfig(object):
    DB_URL = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = '0000'
    DB_DATABASE = 'pythondb'
    DB_CHARSET = 'utf8'
    DB_LOG_FLAG = 'True'                    