no = 10

if no > 5:                        # 일반적인 형태의 if 조건문
    re = no * 2
else:
    re = no + 2
print(re)

re = no * 2 if no > 5 else no + 2  # 삼항 연산 형태의 if 조건문
print(re)   # if 조건이 True이므로 no * 2한 값이 출력

a = 'kbs'
b = 9 if a == 'kbs' else 11
print('b : ', b)
