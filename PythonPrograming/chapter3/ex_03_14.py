while True:      # 이제 조건은 항상 참이 된다.
    a = int(input("확인할 숫자:"))

    if a == 0:   # 키보드에서 0을 입력한 경우
        print("프로그램을 종료합니다.")
        break
    elif a % 2 == 0:
        print("%d는 짝수랍니다." %(a))
    elif a % 2 == 1:
        print("%d는 홀수입니다." %(a))
