#############################
#파이썬 기본 - 반복문
#############################
print('='*100)
a = [1,2,3,4,5]

for num in a:
    print ( num )

a = [(1,2), (3,4), (5,6)]

for i,j in a:
    print( i, j )

a = range( 1, 10 )
print ( a ) 

# range(x,y) => x <= n <y
for num in range( 1, 10 ):
    print (num)

# 3~7단까지 구구단 ( 3 X 1 = 3, ...)


for x in range( 3, 8 ):
    for y in range( 1, 10 ):
        print ("%s X %s = %2s" % (x,y,x*y))

# 축약하여서 리스트로 출력
print( [ x*y for x in range( 3, 8 ) for y in range( 1, 10 ) ])
