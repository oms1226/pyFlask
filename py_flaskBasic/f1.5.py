# 동적파라미터 : URL 경로에 데이터를 전달한다.
# 보안에 문제되지 않는 데이터

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome Flask World'

# ~/users/유저아이디, ~/users/ui2939
# 동적 파라미터는 함수의 인자를 통해서 전달된다.
# <userId> => 문자열로 간주
@app.route('/users/<userId>')
def users(userId):
    #http://127.0.0.1:5000/users/oms1226 --> users is oms1226
    return 'users is %s' % userId

# 타입 제약
# int, float, path
@app.route('/news/<int:newsid>/<int:start>')
def news(newsid, start):
    #http://127.0.0.1:5000/news/13123/1331 --> 뉴스 is 13123 1331
    #http://127.0.0.1:5000/news/13123/fkljfdk --> Not Found
    return '뉴스 is %s %s' % (newsid, start)

@app.route('/p/<path:id>')
def p(id):
    #http://127.0.0.1:5000/p/13123/fkljfdk/test --> p is 13123/fkljfdk/test
    #return 'p is %s' % id
    print(type(id))
    data = id.split('/')
    print (data)
    for d in data:
        print (d)
    return 'p is %s' % id

if __name__ == '__main__':
    app.run(debug=True)
else:
    print('본 서버는 메인으로 구동시에만 작동된다.')