colors = ['red', 'green', 'blue', 'yellow']   # 리스트 형 자료
a = 0

while a < len(colors):              # colors의 크기 만큼 반복 처리
    print('colors : ', colors[a])   # colors 값이 차례대로 출력
    a = a + 1

print('colors 크기 : ', len(colors))

while colors:       #colors에 값이 있는 동안 조건은 True
    colors.pop()
    #print(colors.pop())

print('colors 크기 : ', len(colors))
