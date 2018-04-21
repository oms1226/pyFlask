# 1. 모듈가져오기
from flask import Flask
# 2. 플라스크 생성
app = Flask(__name__)
# 3. 라우팅 (요청 URL을 분석하여 누가 처리할 것인지 매칭 연결)
@app.route('/')
def home():
    return 'Welcome Flask World'
# 4. 서버가동
if __name__ == '__main__':
    app.run(debug=True)
else:
    print('본 서버는 메인으로 구동시에만 작동된다.')