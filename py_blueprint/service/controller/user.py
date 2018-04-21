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