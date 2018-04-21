#############################
#파이썬 기본 - 블린
#############################
# 기호 : True, False
# False : None(null 에 대비), 0, 연산결과가 False
#          [], (), {} : 시퀸스 타입에 데이터가 없다.
print('='*100)
a = [1,2,3,4,5]
# a의 멤버가 업을 때까지 하나씩 뽑아서 출력하시오
while a:
    print( a.pop() )
else:
    print( " 작업 종료 확인 ")

#############################
# 모든 것은 객체다 --> 참조수 검토
import sys
a = 1
print( a, type(a), sys.getrefcount(1) )
b = 1
print( b, type(b), sys.getrefcount(1) )#print나 type 등에서도 변수에 대한 ref count를 잡고 있다.
del(a)#del을 통해 참조를 끊을 수 있다.
print( sys.getrefcount(1) )
del(b)
print( sys.getrefcount(1) )
print(a, b)#NameError: name 'a' is not defined
