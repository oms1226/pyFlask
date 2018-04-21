# 회원 관련 기능 제공
# ~/users/~

# 요청 응답 관련 모든 내용이 포함
from flask import render_template, request, redirect, url_for
# 라우트 담당
from service.app_blueprint import blueprintUser
# 디비 담당
from service.app_database import dao
from service.model.user import User

# ~/users/
@blueprintUser.route('/')
def root():
    print('회원 서비스 메인')
    return '회원 서비스 메인'

@blueprintUser.route('/join/<name>/<password>')#http://127.0.0.1:81/users/join/test/testpwd
def join(name, password):
    print('회원 서비스 가입')
    newUser = User( name, password )
    dao.add( newUser )
    dao.commit()
    return '회원 서비스 가입'

@blueprintUser.route('/update/<_name>/<newname>')#http://127.0.0.1:81/users/update/test/newtest
def update(_name, newname):
    print('회원 서비스 수정')
    #해당 이름을 가진 데이터를 획득
    findUser = dao.query(User).filter_by(name=_name).first()
    print ( findUser )
    findUser.name = newname
    dao.commit()
    return '회원 서비스 수정'

@blueprintUser.route('/login/<name>/<password>')#http://127.0.0.1:81/users/login/newtest/testpwd
def login(name, password):
    print('회원 서비스 로그인')
    #해당 이름을 가진 데이터를 획득
    findUser = dao.query(User).filter_by(name=name, password=password).first()
    print ( findUser )
    if findUser:
        return '회원 서비스 로그인 성공'
    else:
        return '회원 서비스 로그인 실패'

@blueprintUser.route('/delete/<name>/<password>')#http://127.0.0.1:81/users/delete/newtest/testpwd
def delete(name, password):
    print('회원 서비스 탈퇴')
    #해당 이름을 가진 데이터를 획득
    findUser = dao.query(User).filter_by(name=name, password=password).first()
    print ( findUser )
    if findUser:
        dao.delete(findUser)
        dao.commit()
        return '회원 서비스 탈퇴 성공'
    else:
        return '회원 서비스 탈퇴 실패'
