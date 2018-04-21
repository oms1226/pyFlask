# 라우트
## 클라이언트의 요청의 URL을 보고 어떤 함수가 처리할 것인지(응답)
## 연결해주는 기능(라우팅)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome Flask World'

# ~/login
@app.route('/login')
def login():
    return '로그인 페이지'

if __name__ == '__main__':
    app.run(debug=True)
else:
    print('본 서버는 메인으로 구동시에만 작동된다.')