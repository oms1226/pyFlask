# 클래스 형태: 커넥션 풀링은 배제함
import pymysql as my

class DBManager:
    conn = None
    def __init__(self):
        print('생성자 호출')
        self.initDB()
    def initDB(self):
        print('디비 연결 초기화')
        # 연결
        self.conn = my.connect(host='localhost',
                                    user='root',
                                    password='0000',
                                    db='pythondb',
                                    charset='utf8',
                                    cursorclass=my.cursors.DictCursor)
    def freeDB(self):
        print('디비 연결 종료')
        if self.conn:
            self.conn.close()
    def login(self, uid, upw):
        row = None
        # 쿼리
        if self.conn:
            # with문을 사용하면 작업 완료 후 자동으로 close() 해준다
            with self.conn.cursor() as cursor:
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
        return row

if __name__ == "__main__":
    obj = DBManager()
    print( '함수콜:', obj.login('ncia', '1234') )
    print( '함수콜:', obj.login('ncia', '12341') )    
    obj.freeDB()