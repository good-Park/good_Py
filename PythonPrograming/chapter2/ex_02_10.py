aa = [1, 2, 3, 4, 5]
print(aa[0:2]) 

aa = [1, 2, 3, ['a', 'b', 'c'], 4, 5]  # 중첩 리스트도 가능
aa[0] = 100     # 리스트는 요소값 변경이 가능
aa[3][0] = 'good';
print(aa)
print(aa[0], aa[3])
print(aa[3][:2])
print(aa[3][2])

# 리스트 내의 요소 값을 삭제할 수도 있다.
aa.remove(4)   # 값으로 삭제: 4는 값이다.
del aa[4]       # 순서로 삭제: 4는 네번째 위치의 자료다.
print(aa)
aa[3].remove('c')
del aa[3][0]
print(aa)
