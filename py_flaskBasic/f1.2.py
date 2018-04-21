from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome Flask World'

if __name__ == '__main__':
    app.run(debug=True)
else:
    print('본 서버는 메인으로 구동시에만 작동된다.')