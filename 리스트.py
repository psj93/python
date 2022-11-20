#직접 데이터를 넣어 초기화
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

#네번째 원소만 출력
print(a[3])

#크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)

#리스트의 인덱싱과 슬라이싱
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#여덟 번째 원소만 출력
print(a[7])

#뒤에서 첫 번째 원소 출력
print(a[-1])

#뒤에서 세 번째 원소 출력
print(a[-3])

#네 번째 원소 값 변경
a[3] = 7
print(a)

#두 번째 원소부터 네 번째 원소까지
print(a[1:4])

#리스트 컴프리헨션
#0부터 9까지의 수를 포함하는 리스트
array = [i for i in range(10)]
print(array)

#0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)

#1부터 9까지의 수들의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1, 10)]
print(array)

#N x M 크기의 2차원 리스트 초기화
n = 4
m = 3
array = [[0] * m for _ in range(n)]
print(array)

#언더바 사용 : 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 자주 사용함
#1부터 9까지의 자연수를 더하기
summary = 0
for i in range(1, 10):
  summary += i
print(summary)

#"Hello World"를 5번 출력하기
for _ in range(5):
  print("Hello World")

#리스트 관련 기타 메서드
#append() : 변수명.append() : 리스트에 원소를 하나 삽입할 때 사용한다.
#sort() : 변수명.sort() : 기본 정렬 기능으로 오름차순으로 정렬한다.
#         변수명.sort(reverse=True) : 내림차순으로 정렬한다.
#reverse() : 변수명.reverse() : 리스트의 원소의 순서를 모두 뒤집어 놓는다.
#insert() : insert(삽입할 위치 인덱스, 삽입할 값) : 특정한 인덱스 위치에 원소를 삽입할 때 사용한다.
#count() : 변수명.count(특정 값) : 리스트에서 특정한 값을 가지는 데이터의 개수를 셀 때 사용한다.
#remove() : 변수명.remove(특정 값) : 특정한 값을 갖는 원소를 제거하는데, 값을 가진 원소가 여러 개면 하나만 제거한다.


a = [1, 4, 3]
print("기본 리스트 : ", a)

#리스트에 원소 삽입
a.append(2)
print("삽입: ", a)

#오름차순 정렬
a.sort()
print("오름차순 정렬: ", a)

#내림차순 정렬
a.sort(reverse = True)
print("내림차순 정렬 : ", a)

a = [4, 3, 2, 1]

#리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기: ", a)

#특정 인덱스에 데이터 추가
a.insert(2,3)
print("인덱스 2에 3 추가: ", a)

#특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수: ", a.count(3))

#특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제: ", a)

#리스트에서 특정값을 가지는 원소를 모두 제거하기
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5} #집합 자료형

#remove_list에 포함되는 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)
