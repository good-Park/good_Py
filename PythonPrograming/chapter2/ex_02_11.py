aa = [3, 1, 5, 2, 4]
aa.sort();               # 오름차순으로 정렬
print('sort 결과:', aa)
aa.sort(reverse=True);   # 내림차순으로 정렬
print('reverse 결과:', aa)

aa2 = ['123', '34', '234']  # 숫자 형태의 문자열을 기억
print(aa2)              # 입력된 순서 그대로 출력
aa2.sort()              # 문자열이므로 사전순으로 정렬
print(aa2)
aa2.sort(key=int)       # 문자열이지만 숫자형으로 정렬
print(aa2)

aa2 = [3, 1, 2]
aa3 = sorted(aa2)       # 새로운 기억 장소에 정렬 결과가 기억
print(aa2)
print(aa3)
