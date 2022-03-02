mydic = dict(k1 = 1, k2 = 'abc', k3 = 3.4)   # dict 함수 사용
print(mydic)                 # 딕셔너리 형으로 출력

# {'키1' : '값1', …} 의 형태로 딕셔너리를 만들 수도 있다.
coffee = {'mocha':'카페모카', 'latte':'라떼'}
print(coffee)
print('coffee의 크기는 ', len(coffee))
print(coffee['mocha'])         # 키를 이용해 값을 조회
# print(coffee['카페모카'])     # 값으로 조회하면 에러!

print(coffee.keys())          # key 목록을 출력
print(coffee.values())        # value 목록을 출력
print(coffee.items())         # key, value 모두를 출력

print(list(coffee.keys()))    # key를 리스트로 출력
print(list(coffee.values()))  # value를 리스트로 출력

print(coffee.get('latte'))    # key로 value 얻기

print('latte' in coffee)      # key의 유무를 판단

coffee['lungo'] = '룽고'       # 요소를 추가
print(coffee)
del coffee['lungo']            # 요소를 삭제
print(coffee)

drink = {'cola':'콜라'}         # 딕셔너리형 자료 병합
water = {**coffee, **drink}
print(water)