# db 연동
# python + mysql 연동
# pip install pymysql
# 차후에는 sqlAlchemy 모듈을 설치하여 pymysql을 Wrapping 하여 사용
import pymysql as my

# 연결
connection = my.connect(host='localhost',
                             user='root',
                             password='0000',
                             db='pythondb',
                             charset='utf8')
print('연결성공')
# 연결 종료
connection.close()
print('연결종료')