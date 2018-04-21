#############################
#파이썬 기본 - 모듈 호출
#############################
print('='*100)
#모듈 가져오기
from p1_13 import SubClass

obj = SubClass('hi')
print ( obj.name )
print ( obj.name, obj.getName() )

from a import sum
print( sum(1,2) )

from a.b.test import PI
print( "PI: %s" % PI)

# as 별칭
import a.b.test as t
print (t.PI)

from a.b import *
print ( test.PI )