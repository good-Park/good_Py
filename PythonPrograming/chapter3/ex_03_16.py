chars = []     # 리스트 형 변수 선언
sentence = '파이썬은 기능이 좋은 언어'

for k in sentence:
    chars.append(k)   # sentence 변수에 문자열이 한 글자씩 차례대로 리스트에 저장

print(chars)

for k in chars:       # chars 요소 수만큼 반복 처리
    if k != ' ':      # 공백을 제외한 문자 출력용 조건문
        print(k, end='')
