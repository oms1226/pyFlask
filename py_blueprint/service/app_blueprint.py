# 회원관련 api, 웹페이지는
# ~/users/~
# 주식
# ~/trade/~

from flask import Blueprint
# 회원 관련 블루프린트
blueprintUser = Blueprint(
    'user_blue',
    __name__,
    template_folder='templates',
    static_folder='static'
)

# 주식 관련 블루프린트
blueprintTrade = Blueprint(
    'trade_blue',
    __name__,
    template_folder='templates',
    static_folder='static'
)