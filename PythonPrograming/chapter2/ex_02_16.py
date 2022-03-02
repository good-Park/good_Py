# 세트 자료형은 중복 자료 제거한다.
a = {1, 2, 3, 1}
print('set(a)는', a)
print('tuple(a)는', tuple(a))    # 튜플로 형변환
print('list(a)는', list(a))      # 리스트로 형변환

li = [1, 2, 2, 3, 1]        # 1과 2가 2번 들어 있다.
print('리스트 li는', li)

s = set(li)     # 세트로 형변환하면 중복된 자료가 없어짐.
li = list(s)    # 세트를 다시 리스트로 형변환한다.
print('변환 후 li는', li)
