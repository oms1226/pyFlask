# pip install selenium

from selenium import webdriver as wd

# 타켓 사이트 지정 (PC 웹, 모바일웹)
target_url = 'http://tour.interpark.com/'

# 브라우져 띠우기
# 에이전트 변조, 프록시 우회, 이미지는 제외하겠금 로드
driver = wd.Chrome(executable_path='./chromedriver.exe')

# 페이지로드
driver.get( target_url )