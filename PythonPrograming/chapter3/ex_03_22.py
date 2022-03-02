a = 0
b = 1

for n in range(0, 11):  # 11회 반복 수행한다.
    print(a)
    temp = a
    a = b
    b = temp + b    # b는 두 수의 합을 기억하게 된다.



