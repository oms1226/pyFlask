# 주식 관련 기능 제공
# ~/trade/~

# 요청 응답 관련 모든 내용이 포함
from flask import render_template, request, redirect, url_for
# 라우트 담당
from service.app_blueprint import blueprintTrade as trade
# 디비 담당
from service.app_database import dao

# ~/trade/
@trade.route('/')
def root():
    print('주식 서비스 메인')
    return '주식 서비스 메인'