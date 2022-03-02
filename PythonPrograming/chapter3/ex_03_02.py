nums = 1, 2, 3     # 튜플에 숫자들을 기억
if 2 in nums:      # nums에 2가 있으면 True 없으면 False가 된다.
    print('있어요')
else:
    print('없어요')

if 2 not in nums:  # nums에 2가 없으면 True 있으면 False가 된다.
    print('없군요')
else:
    print('있군요')

names = ['홍길동', '신선해', '이기자']   #리스트에 문자열을 기억시킨다.
if '홍길동' in names:       # names에 '홍길동' 유무로 조건 처리
    print('내 친구야')
else:
    print('넌 누구?')
