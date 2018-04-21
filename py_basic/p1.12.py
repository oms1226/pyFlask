#############################
#파이썬 기본 - class
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
    '''
    멤버함수
    '''
    def getName(self):
        return self.name

# 객체 생성
obj = MyClass('양재')
print( obj.name, obj.getName())