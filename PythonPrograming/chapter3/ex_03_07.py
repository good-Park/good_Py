jumsu = int(input('점수 입력:'))     # 형변환 함수 사용 int() 사용

if jumsu >= 90 and jumsu <= 100:   # 두 개의 조건에 and를 사용
    result = "A"
    score = 1
elif 80 <= jumsu < 90:            # 조건식을 간결하게 적을 수 있다.
    result = "B"
    score = 2
else:
    result = "C"
    score = 3

print('result : ', result)
print('result : ' + str(score))  # str() 함수로 숫자를 문자열로 변환
