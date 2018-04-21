# 정적 파일 위치
# /static
## html, css, js, images, 업로드파일
# 라우트가 필요 없다.
#http://127.0.0.1:5000/static/images/a.jpg
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome Flask World'

# url 요청 테스트
with app.test_request_context():
    print( url_for('static', filename='images/a.jpg') )  

if __name__ == '__main__':
    app.run(debug=True)
else:
    print('본 서버는 메인으로 구동시에만 작동된다.')