a = {1, 2, 3, 1}
print(a)
print('a의 크기는 ', len(a))

b = {3, 4}

print('a와 b의 합집합:', a.union(b))
print('a와 b의 교집합:', a.intersection(b))
print('a와 b의 차집합:', a.difference(b))

print('합집합(a | b):%s'%(a | b))
print('교집합(a & b):%s'%(a & b))
print('차집합(a - b):%s'%(a - b))

#print(b[0])     # 에러: 세트는 인덱싱이 불가능
b.add(5)         # 요소 추가
print('요소를 추가한 후 b는', b)

b.update({6, 7})    # b = u U {6, 7} 한 결과를 갖는다.
b.update([8, 9])    # 리스트의 자료로도 수정이 가능
b.update((10, 11))  # 튜플의 자료로도 수정이 가능
print('update 후 b는', b)

b.discard(7)        # 요소 삭제: 값 7을 삭제(없으면 통과)
b.remove(6)         # 요소 삭제: 값 6을 삭제(없으면 에러)
print('\n요소 삭제 후 b는', b)
