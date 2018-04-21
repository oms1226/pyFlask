#############################
#파이썬 기본 - 시퀸스 타입 - 리스트 []
#############################
# 순서가 있다. 배열을 연상, 인덱스 존재, 값의 중복 관계 없다.
print('='*100)
# 비워있는 리스트
odd = []
print( odd )
odd = [1,2,3,4]
print( odd )
ani = ['cat', 'dog', 'bird']
print( ani )
# 타입이 다를 경우 (리스트의 멤버) => 타입은 달라도 상관없다
mix = [1, 2, "man"]
print( mix )
matrix = [1,2,[3,4]]
print( matrix )

#############################
print('='*100)
# 인덱싱 => [인텍스]
print( matrix[1], matrix[2][0] )
# 슬라이싱 => [:]
a = [1,2,3,4,5,6,7,8,9]
# 원복 복사
# [시작인덱스:끝인덱스:step(안쓰면1)]
print( a[:], a[:3], a[1:-1], a[1:-1:2] )

#############################
# 리스트 더하기 (두개가 차례대로 이어져서 연속된 리스트의 사본을 반납)
print( a + mix )
# 반복
print( a * 5 )
# 수정(원본)
a[1] = 100
print( a )
#a[1:3] = 99#TypeError: can only assign an iterable
a[1:3] = ani
print( a )
a[1] = ani
print( a )

#############################

#삭제
a = [1,2,3,4,5]
print( a )
del a[1]
print( a )

# 전체삭제
del a[:]#a.clear()
print( a )

# 추가
a.append(1)
a.append(1)
a.append("2")
print( a )
# 값을 넣어서 삭제 => 최초로 만나는 값을 한개 제거한다
a.remove(1)#1이라는 값을 삭제한다.
print( a )

#############################
a = [1,5,32,7,8,4,3,896,4,8,95,3]
a.sort()#원복 조작
print( a )
print( a.pop() )
print( a )