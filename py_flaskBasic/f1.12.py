# 폼 업로드 (파일 업로드 및 글쓰기)
# 데이터가 전달되면, 파일 업로드 -> url 경로획득 -> DB에(제목, 내용, 경로) 입력
# 리스트까지 뿌리면(?)
from flask import Flask, request, render_template, redirect, url_for
import os
from dbMgr import DBManager

app = Flask(__name__)
dbMgr = DBManager()

@app.route('/')
def home():
    # 홈페이지 접속을 해도 바로 /upload로 포워딩함
    return redirect( url_for('upload') )

@app.route('/upload', methods=["get","post"])
def upload():
    #print( "pwd:", os.getcwd(), request.method )
    #print( os.getcwd() + "\\static\\upload\\" + "파일명(확장자포함)")
    #if request.method == 'get':
    # method에는 소문자를 써도 되지만 비교식에는 대문자만 써야된다!!!!!!!!!!!!!!
    if request.method == 'GET':    
        return render_template( 'upload.html' )
    else:
        #파일 데이터 획득
        fileData = request.files['fileData']#file 이기에 files로 읽었따.
        
        # 저장
        fileData.save( os.getcwd() + "\\static\\upload\\" + fileData.filename)
        title = request.form['title']#text 이기에 form으로 읽었다.
        content = request.form['content']#text 이기에 form으로 읽었다.
        url = url_for('static', filename='upload/'+fileData.filename)
        print( title, content, url )
        if dbMgr.insertNews( title, content, url ) > 0:
            return render_template('errorjs.html', errMsg='완료', path=url_for('home'))
        else:
            return render_template('errorjs.html', errMsg='실패', path=None)            

        #return 'upload proc'
    

if __name__ == '__main__':
    app.run(debug=True)
else:
    print('본 서버는 메인으로 구동시에만 작동된다.')