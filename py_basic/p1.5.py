#############################
#파이썬 기본 - 딕셔너리 {}
#############################
# 순서 X, 키와 값의 세트, 키는 중복되면 안된다.
# 값은 중복되도 상관없음, 키의 타입은? 관계없음
# 디비 쿼리로부터 결과를 받은 row 1개 1개의 타입
print('='*100)
dic = {"name":"kim", "age": 10, 1004:"Yes"}
print( dic )
print( type(dic) )
# 인덱싱 : 인덱스 자리에 키를 넣는다
print( dic[1004])
# 삭제
del dic['age']
print( dic )
print( '리스트로 반환', dic.keys() )
print( '리스트로 반환', dic.values() )
for key in dic.keys():
    print( key, dic[key])
dic.clear()
print( dic )