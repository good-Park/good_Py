s1 = 'kbs mbc'
s1 = ' ' + s1[:4] + 'sbs ' + s1[4:] + ' '
print(s1)

print('공백 제거 ', s1.strip())
s2 = s1.split(sep = ' ')  # 공백을 구분자로 문자열 분리
print(s2)
print('-'.join(s2))       # 하이픈(-)을 구분자로 문자열을 결합

ss = '대한민국 만세'
print(ss.replace('대한민국', '파이썬'))  # 문자열의 일부를 치환
