# restful
# ~/login: 로그인 폼   : GET
# ~/login: 로그인 처리 : POST
from flask import Flask, request, render_template, url_for, jsonify
from dbMgr import DBManager

app = Flask(__name__)
dbMgr = DBManager()

@app.route('/')
def home():
    rows = dbMgr.getEplInfoAll()
    return render_template('home.html', teams=rows)

# get 방식, post 방식 모두 지원
@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('loginForm.html', action=url_for('login'), title='로그인')
    else:
        # 아이디, 비번 획득
        uid = request.form['uid']
        upw = request.form['upw']
        # 쿼리 수행
        if uid and upw:
            #디비 쿼리
            row = dbMgr.login(uid, upw)
            #return 'login POST uid: %s, upw:%s' % (uid, upw)            
            if row:
                return render_template('errorjs.html', errMsg='로그인성공', path=url_for('home'))
            else:
                return render_template('errorjs.html', errMsg='아이디나 비번이 틀립니다.', path=None)
        else:
            print('비정상 경로로 접근하였다')
            #return "<script>alert('로그인오류');history.back();</script>"
            return render_template('errorjs.html', errMsg='로그인오류', path=None)
        # 결과에 따른 분기 처리
        #return 'login POST uid: %s, upw:%s' % (uid, upw)        

@app.route('/search', methods=['post'])
def search():
    print('검색요청')
    # 검색어 추출
    keyword = request.form['keyword']
    # 검색
    rows = dbMgr.searchWithKeyword(keyword)
    # json 응답
    return jsonify( rows )
    
    

if __name__ == '__main__':
    app.run(debug=True)
else:
    print('본 서버는 메인으로 구동시에만 작동된다.')