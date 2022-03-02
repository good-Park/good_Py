# 스택 구현
print('리스트로 stack(LiFO) 처리')
sbs = [10, 20, 30]
sbs.append(40)    # sbs 변수에 요소를 추가
print(sbs)
sbs.pop();        # sbs변수의 마지막 요소를 제거
print(sbs)
sbs.pop();        # sbs변수의 마지막 요소를 제거
print(sbs)

# 큐 구현
print('리스트로 queue(FiFO) 처리')
sbs = [10, 20, 30]
sbs.append(40)
print(sbs)
sbs.pop(0);       # sbs 변수의 첫번째 요소를 제거
print(sbs)
sbs.pop(0);       # sbs 변수의 첫번째 요소를 제거
print(sbs)
