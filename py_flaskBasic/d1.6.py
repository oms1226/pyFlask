# db 연동
# python + mysql 연동
# pip install pymysql
# 차후에는 sqlAlchemy 모듈을 설치하여 pymysql을 Wrapping 하여 사용
import pymysql as my

# 함수 형태로 전환 -> 아이디, 비번만 전달되면 로그일을 수행할 수 있게
def login(uid, upw):
    row = None
    # 연결
    conn = my.connect(host='localhost',
                                user='root',
                                password='0000',
                                db='pythondb',
                                charset='utf8',
                                cursorclass=my.cursors.DictCursor)

    # 쿼리
    if conn:
        # with문을 사용하면 작업 완료 후 자동으로 close() 해준다
        with conn.cursor() as cursor:
            sql = '''
                select
                    *
                from
                    users
                where
                    uid=%s
                and
                    upw=%s;
                    '''
            aff_row = cursor.execute( sql, (uid, upw) )
            row = cursor.fetchone()

        conn.close()
    
    return row

if __name__ == "__main__":
    print( '함수콜:', login('ncia', '1234') )
    print( '함수콜:', login('ncia', '12341') )    