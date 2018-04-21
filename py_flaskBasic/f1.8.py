# restful
# ~/login: 로그인 폼   : GET
# ~/login: 로그인 처리 : POST
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome Flask World'

# get 방식, post 방식 모두 지원
@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return 'login GET'
    else:
        return 'login POST'

if __name__ == '__main__':
    app.run(debug=True)
else:
    print('본 서버는 메인으로 구동시에만 작동된다.')