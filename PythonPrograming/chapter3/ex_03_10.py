a = 1              # while 조건에 사용할 변수에 1을 기억
hap = 0            # 짝수의 합을 구하기 위한 누적용 변수

while a <= 10:     # 조건이 참인 동안 반복 처리
    print(a, end = ' ')

    if a % 2 == 0:   # while문 안에 if문 사용
        hap += a     # a 값이 짝수인 경우에 누적
    a += 1           # while 조건이 거짓이 될 수 있도록 1씩 증가

print('\n짝수의 합은 ' + str(hap))
