# /pro  -> /pro/
# /pro/ -> /pro/
# 자동 처리된 곳 => 홈페이지

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome Flask World'

@app.route('/pro/')
def pro():
    return 'pro'

if __name__ == '__main__':
    app.run(debug=True, port=80)
else:
    print('본 서버는 메인으로 구동시에만 작동된다.')