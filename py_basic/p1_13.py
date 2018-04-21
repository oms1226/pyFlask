#############################
#파이썬 기본 - class 상속
#############################
# 자기 자신 객체 -> self
# 맴버함수 맴버변수, 생성자
print('='*100)

class MyClass:
    '''
    멤버 변수
    '''
    name = None
    '''
    생성자
    '''
    def __init__(self, name):
        self.name = name
        print('부모 생성자 호출')
    '''
    멤버함수
    '''
    def getName(self):
        print('부모 getName 호출')
        return self.name

# 자식 클래스
class SubClass(MyClass):
    # 생성자
    def __init__(self, name):
        self.name = name + " : 자식"
        print('자식 생성자 호출')
    # 맴버함수 재정의
    def getName(self):
        print('자식 getName 호출')
        super().getName()
        return self.name + " : 재정의"

print("__name__ = %s" % __name__)#다른 곳에서 호출되면, __name__ = p1_13 값이 출력된다!
# 객체 생성
# 모듈로 사용될 경우와 메인으로 사용할 경우를 분리하여 코드 처리가 필요
if __name__ == "__main__":
    obj = SubClass('양재')
    print( obj.name, obj.getName())
else:
    print('본 내용이 보이면 본 코드를 모듈로 사용한 것이다')