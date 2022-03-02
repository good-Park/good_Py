jumsu = 60

if jumsu >= 90:
    print('우수')      # 첫 번째 조건이 참이면 수행
else:
    if jumsu >= 70:   # else 영역에 중첩if문 사용
        print('보통')  # 첫 번째 조건이 거짓, 두 번째 조건이 참이면 수행
    else:
        print('저조')  # 첫 번째 조건이 거짓, 두 번째 조건이 거짓이면 수행

if jumsu >= 90:
    pass              # 첫 번째 조건이 참인 경우 수행문이 없다.
else:
    if jumsu >= 70:
        pass          # 첫 번째 거짓, 두 번째 참인 경우 수행문이 없다.
    else:
        print('난 언제 처리될까')  # 첫 번째, 두 번째 모두 거짓인 경우
