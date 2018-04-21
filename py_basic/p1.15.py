#############################
#파이썬 기본 - 예외처리
#############################
print('='*100)
try:
    print("1")
    a = 1/0
    print("2")
except Exception as e:
    print("3")
    print(e)
finally:
    print("4")