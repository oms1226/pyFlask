# db 연동
# python + mysql 연동
# pip install pymysql
# 차후에는 sqlAlchemy 모듈을 설치하여 pymysql을 Wrapping 하여 사용
import pymysql as my

# 연결
conn = my.connect(host='localhost',
                             user='root',
                             password='0000',
                             db='pythondb',
                             charset='utf8',
                             cursorclass=my.cursors.DictCursor)
print('연결성공')

# 쿼리
if conn:
    # 1. 커서 획득
    cursor = conn.cursor()
    if cursor:
        # 2. sql 준비
        sql = "select * from users where uid=%s and upw=%s;"
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
        # 3. 쿼리 수행
        aff_row = cursor.execute( sql, ('ncia', '1234') )
        print( aff_row )
        # 4. 결과 획득 -> 1개 데이터
        row = cursor.fetchone()
        print( row )

        # 5. 커서 닫기
        cursor.close()

    # 연결 종료
    conn.close()
    print('연결종료')