money = 1000   # money 값은 동적
age = 23       # age 값은 동적

if money >= 500:        # 첫 번째 조건식이 참인 경우 처리
    item = 'apple'      # 첫 번째 조건이 참이면 수행
    if age <= 30:       # 중첩if문. 첫 번째 조건 내의 두 번째 조건문
        msg = 'young'   # 첫 번째, 두 번째 조건이 모두 참이면 수행
    else:
        msg = 'old'   # 첫 번째 조건 참, 두 번째 조건 거짓이면 수행

else:                 # 첫 번째 조건식이 거짓인 경우 처리
    item = '사과'      # 첫 번째 조건이 거짓이면 수행
    if age >= 20:     # 중첩if문.
        msg = '어른'   # 첫 번째 조건 거짓, 두 번째 조건 참이면 수행
    else:
        msg = '아이'   # 첫 번째, 두 번째 조건이 모두 거짓이면 수행

print(item, msg)
