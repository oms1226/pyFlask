# 상용 모드 및 디버그 모드 구동하기
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome Flask World'

if __name__ == '__main__':
    #상용 모드 => 소스 변화에 의한 재가동 불가. 운용 시에만 사용
    #app.run()
    #디버깅 모드1 => 소스 변화 감지, 상세한 로그 제공 => 운용 시 사용하면 안됨
    #app.run(debug=True)
    #디버깅 모드2 => 미감지대상( 정적파일, html, css, js, image , ...) --> 그래서 리플래쉬 하면된다.
    app.debug = True
    app.run()
else:
    print('본 서버는 메인으로 구동시에만 작동된다.')