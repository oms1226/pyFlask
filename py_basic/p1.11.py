#############################
#파이썬 기본 - 함수
#############################
print('='*100)
# 기본형
def sum(a, b):
    return a+b

print ( sum(1, 2) )

# 가변인자
def sumEx(*params):
    # 수치형만 들어오고 들어온 파라미터를 다 더한다고 한다면,
    sum = 0
    print ( type(params) )
    for n in params:
        sum += n
    return sum
print( sumEx(1,2,3,4,5,6) )
print( sumEx(1,2,3,4) )

# 인자값 초기화
# 인자값에 기본값을 부여하여, 호출 시 데이터를 보내지 않아도 자동 처리된다.
def person(name, age, height=100):
    print( name, age, height )

print( person( 'kim', 20, 180) )
print( person( 'kim', 30) )


def sumEx2(*params):
    # 수치형만 들어오고 들어온 파라미터를 다 더한다고 한다면,
    sum = 0
    mul = 1
    print ( type(params) )
    for n in params:
        sum += n
        mul *= n
    return sum, mul

print( sumEx2(1,2,3,4,5) )