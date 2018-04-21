'''
- blueprint with flask 웹기반 서비스 개발
- blueprint : flask안에 있는 기능
- blueprint -> url 기반에 prefix를 제공하여 기능별로 개발가능하게 지원
  회원 : ~/users/~
  뉴스 : ~/news/~
'''
# 모듈 가져오기
from service import create_app

# 서버 생성
app = create_app()

# 구동
if __name__ == '__main__':
    # 서버측 정보를 좀더 세밀하게 기술
    # 개발서버
    ##'0.0.0.0' 이라는 것은 존재하지 않기에 locathost로 설정된다.
    app.run(host='0.0.0.0', port=81, debug=True)
    # 상용서버
    #app.run(host='0.0.0.0', port=80, debug=False)