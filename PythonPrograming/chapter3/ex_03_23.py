for i in range(6):   # 0~5까지 6회 반복
    print(i, end=' ')

print()
for _ in range(1, 3):
    print('안녕')

# 1~10까지 합 계산
tot = 0
for i in range(1, 11):
    tot += i     # 1~10까지 차례로 기억한 i 값은 tot에 누적
print('합은 : ' + str(tot))

matrix = [[1, 2, 3], [4, 5, 6]];  # 중첩 리스트 값(2행3열) 출력
for m in range(2):                # 0~1행 처리는 m이 기억해 반복 처리
    for n in range(3):            #  0~2열 요솟 값은 n이 기억해 반복 처리
        print(matrix[m][n], end = ' ')
    print()
