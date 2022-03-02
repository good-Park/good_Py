s = 'sequence'    # 변수 s는 문자열 'sequence'를 기억한다.

print('길이(크기) : ', len(s))
print('포함 횟수 : ', s.count('e'))
print('검색 위치 : ', s.find('e'), s.find('e', 3), s.rfind('e'))
print('첫 글자 유무 : ', s.startswith('s'), s.startswith('a'))
print('해당 요소값 유무 : ', 'e' in s)

# 인덱싱과 슬라이싱 처리
print(s[0], ' ', s[7])     # 0번째, 7번째 값 출력
print(s[1:], ' ', s[1::2])
print(s[:3], ' ', s[3:])
print(s[-1], ' ', s[-8])
print(s[-4:], ' ', s[::3])
print(s[1:7:1], ' ', s[1:7])   # 둘의 결과는 같다.

print('값 변경 전 : ', id(s))
s = 'fre' + s[2:]    # 슬라이싱을 이용한 변경, 수정이 아니다.
print(s)             # 새 객체의 주소를 참조하게 된다.
print('값 변경 후 : ', id(s))
