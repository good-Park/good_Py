for i in [1, 2, 3, 4, 5]:                # 리스트에 저장된 숫자 요소 수만큼 반복 처리
    print(i, end=' ')
print()

for c in ['red', 'green', 'blue']:       # 리스트에 저장된 문자열 요소
    print(c, end=' ')
print()

for n in {'one', 'two', 'three'}:        # 세트 요소 출력(순서 동적)
    print(n, end=' ')                    # 순서가 없으므로 출력 결과는 매번 다름
print()

for t in ('house', 'mouse', 'horse'):    # 튜플 요소 출력
    print(t, end=' ')

print()
soft = {'java':'웹용', 'python':'만능', 'oracle':'db'}  # 딕셔너리 요소 출력

for i in soft.items():
    print(i[0] + ', ' + i[1])   # 튜플로 반환된 값을 차례대로 출력

for k in soft.keys():
    print(k, end=' ')           # key만 출력
print()

for v in soft.values():
    print(v, end=' ')           # value만 출력
