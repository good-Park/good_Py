# 얕은 복사
name1 = ['톰', '존']
name2 = name1             # 주소 복사: 같은 객체를 참조

# name1과 name2는 주소가 같다.
print(name1, id(name1))
print(name2, id(name2))
name1[0] = '수잔'          # name1의 0번째 요소를 변경
print(name1)
print(name2)              # name1의 출력 결과와 같다.

# 깊은 복사
import copy                # deepcopy()를 지원하는 모듈 로딩
name3 = copy.deepcopy(name1)    # 별도의 공간을 확보
name1[0] = '폴'            # name1의 0번째 요소를 변경
print(name1, id(name1))
print(name2, id(name2))   # name1의 출력 결과와 같다.
print(name3, id(name3))   # name1의 출력 결과와 다르다.
