v1, *v2 = 1, 2, 3, 4, 5   # 값 할당 packing 연산을 수행한다.
print(v1)
print(v2)

*v1, v2 = 1, 2, 3, 4, 5   # packing을 위한 변수의 위치를 변경
print(v1)
print(v2)

*v1, v2, v3 = 1, 2, 3, 4, 5   # v1 변수만 packing 처리한다.
print(v1)
print(v2)
print(v3)

v1, *v2, v3 = 1, 2, 3, 4, 5   # v2 변수만 packing 처리한다.
print(v1)
print(v2)
print(v3)

# v1, *v2, *v3 = 1, 2, 3, 4, 5  # 에러 : * 연산자는 복수 사용은 불가능
