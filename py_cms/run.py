from flask import Flask, render_template, url_for, request, session, redirect
from dbMgr import DBManager

app = Flask(__name__)
# 세션 생성에 필요한 해쉬값을 넣는다 (길이는 관계 없음)
app.secret_key = "rhljkfghjcfgvbnytgdjkfcakmakjflsafh"#상용에서는 생성기를 사용한다.
info = {}
dbMgr = DBManager()

@app.route('/')
def home():
    # 세션이 없으면, 로그인 페이지로 이동
    if 'userid' in session:
        return render_template('index.html', info=info)        
    else:
        return redirect( url_for('login') )

@app.route('/logout')
def logout():
    # 세션 안에 userid라는 키값이 존재하면
    if 'userid' in session:
        session.pop('userid', None)
    return render_template('errorjs.html', errMsg='로그아웃성공', path=url_for('home'))    

@app.route('/eplList')
def eplList():
    return "eplList"

# get 방식, post 방식 모두 지원
@app.route('/login', methods=['GET','POST'])#/login/ 이라 쓰면 해당 페이지에서 상대경로가 /login/부터 진행되는 문제가 발생한다.
def login():
    if request.method == 'GET':
        return render_template('login.html', action=url_for('login'))
    else:
        # 아이디, 비번 획득
        uid = request.form['uid']
        upw = request.form['upw']
        #return "%s %s " % (uid, upw)
        # 쿼리 수행
        if uid and upw:
            #디비 쿼리
            row = dbMgr.login(uid, upw)
            #return 'login PO
            # 
            # ST uid: %s, upw:%s' % (uid, upw)            
            if row:
                # 세션 생성
                session['userid'] = row['uid']
                return render_template('errorjs.html', errMsg='로그인성공', path=url_for('home'))
            else:
                return render_template('errorjs.html', errMsg='아이디나 비번이 틀립니다.', path=None)
        else:
            print('비정상 경로로 접근하였다')
            #return "<script>alert('로그인오류');history.back();</script>"
            return render_template('errorjs.html', errMsg='로그인오류', path=None)
        # 결과에 따른 분기 처리
        #return 'login POST uid: %s, upw:%s' % (uid, upw)      

info['web_title'] = '관리사이트'
info['home_url'] = '/'#url_for('home')

if __name__ == '__main__':
    app.run(debug=True)
else:
    print('본 서버는 메인으로 구동시에만 작동된다.')