datas = [1, 2, 3, 4, 5]

for i in datas:
    if i == 3: continue   # for 문으로 이동
    if i == 4: break      # 반복 처리를 강제 종료
    print(i)

print()

jumsu = [95, 70, 60, 50, 100]
number = 0

for jum in jumsu:
    number += 1   # 순서가 1부터 보이게 하려고 인덱스에 1을 더해 줬다
    if jum < 70: continue  # 70 미만인 값은 출력에서 제외
    print('%d번째 응시자는 합격' % number)
