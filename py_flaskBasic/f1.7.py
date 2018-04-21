# 코드 내에서 url을 직접 부를 것인가(redirect)
# url과 함수는 연결
# 함수를 통해서 url 획득
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home():pass

@app.route('/users/login/')
def users():pass

@app.route('/users/<userID>/')
def users2(userID):pass

# url 요청 테스트
with app.test_request_context():
    print( url_for('home') )
    print( url_for('users') )
    print( url_for('users2', userID='oms1226') )        

if __name__ == '__main__':
    app.run(debug=True)
else:
    print('본 서버는 메인으로 구동시에만 작동된다.')