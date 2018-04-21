#############################
#파이썬 기본 - 집합 (리스트, 튜플 => 중복제거)
#############################
# 중복 제거, 정렬하지 않는다(간혹 될수도 있다)
print('='*100)
a = [6,3,8,45,30,35,457,2,358,2,1,90]
print( a )
b = set( a )
print( b )
c = list( b )
c.sort()
print( c )
##########################################################
# 합집합, 교집합, 차집합
a = set( [1,3,5,7,9] )
b = set( [2,4,6,8,1] )
print('합집합', a.union(b))
print('교집합', a.intersection(b))
print('차집합', a.difference(b), b.difference(a))
##########################################################
a.add(11)
print( a )
a.add(1)
print( a )
a.update([13,15,17])
print(a)
#print( a + b )#TypeError: unsupported operand type(s) for +: 'set' and 'set'
a.remove(11)
print( a )