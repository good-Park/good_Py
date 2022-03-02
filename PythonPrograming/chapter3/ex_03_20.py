price = {'사과': 2000, '감': 500, '바나나': 1000}  # 판매 목록 자료
my = {'사과': 2, '감': 3}              # 내가 구매한 과일 자료

imsi = (f for f in my)

for i in imsi:
    print('키:', i)
    print('값: price는{}, my는{}'.format(price[i], my[i]))

bill = sum(price[f] * my[f] for f in my)
print('구매한 과일 값은 {}원'.format(bill))
