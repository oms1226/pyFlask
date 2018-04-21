# html 랜더링 처리
# Jinja2 엔진 사용
## http://jinja.pocoo.org/docs/2.10/
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<uid>')
def home(uid=None):
    if uid == None:
        return render_template('index.html')        
    else:
        return render_template('index.html', user=uid)

if __name__ == '__main__':
    app.run(debug=True)
else:
    print('본 서버는 메인으로 구동시에만 작동된다.')