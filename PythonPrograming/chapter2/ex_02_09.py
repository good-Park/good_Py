# a는 리스트 변수로 묶음 자료를 참조한다.
a = [1, 2, 3]
print(a)

# 리스트 형은 다양한 데이터를 기억할 수 있다.
b = [10, a, 20.5, True, '문자열']
print(b)
print(id(a), id(b))          # 주소 확인

friends = ['오공', '팔계', '오정']
print('친구 목록 : ', friends)
print('친구 수 : ', len(friends))   # 요소 수 확인
print('세 번째 친구는 ', friends[2])

friends.append('관우')           # 관우 자료를 추가
friends.remove('오공')           # 오공 자료를 삭제
friends.insert(0, '장비')        # 장비 자료를 삽입
friends.extend(['조조', '여포'])  # 여러 자료를 추가
friends += ['손권']              # 손권 자료를 추가
print('친구 목록 :', friends)

print('저팔계는 몇 번째?', friends.index('팔계'))
print('관우 있나?', '관우' in friends)
print('동탁 있나?', '동탁' in friends)

