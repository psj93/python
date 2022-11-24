#이진 탐색 알고리즘
#순차 탐색:리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
#이진 탐색:정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
# 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정함

#이진 탐색 동작 예시
#이미 정렬된 10개의 데이터 중에서 값이 4인 원소를 찾는 예시를 살펴봅시다

0 - 2 - 4 - 6 - 8 - 10 - 12 - 14 - 16 - 18

#step1.시작점:0, 끝점:9, 중간점:4(소수점 이하 제거) <- 인덱스를 의미함
#step2.시작점:0, 끝점:3, 중간점:1(소수점 이하 제거)
#step3.시작점:2, 끝점:3, 중간점:2(소수점 이하 제거)

#이진 탐색의 시간 복잡도
#단계마다 탐색 범위를 2로 나누는 것과 동일하므로 연산 횟수는 log2N에 비례함
#예를 들어 초기 데이터 개수가 32개일 때, 이상적으로 1단계를 거치면 16개 가량의 데이터만 남음
# 2단계를 거치면 8개 가량의 데이터만 남음
# 3단계를 거치면 4개 가량의 데이터만 남음
#다시 말해 이진 탐색은 탐색 범위를 절반씩 줄이며, 시간 복잡도는 O(logN)를 보장함

#이진 탐색 소스코드:재귀적 구현

#이진 탐색 소스코드 구현(재귀 함수)

def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  #찾은 경우 중간점 인덱스 반환
  if array[mid] == target:
    return mid
  #중간점의 값보다 찾고자 하는 값이 적은 경우 왼쪽 확인
  elif array[mid] > target:
    return binary_search(array, target, start, mid - 1)
  #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
  else:
    return binary_search(array, target, mid + 1, end)
  
#n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
#전체 원소 입력 받기
array = list(map(int, input().split()))

#이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print(result + 1)
  
10 7
1 3 5 7 9 11 13 15 17 19
4

10 7 
1 3 5 6 9 11 13 15 17 19
원소가 존재하지 않습니다.

#이진 탐색 소스코드:반복문 구현
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    #찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
      return mid
    #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
      end = mid - 1
    #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
      start = mid + 1
  return None

#n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
#전체 원소 입력 받기
array = list(map(int, input().split()))

#이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print(result + 1)
  
#파이썬 이진 탐색 라이브러리
#bisect_left(a, x):정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
#biset_right(a, x):정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

    1    2    4    4    8
           ^         ^
           |         |
 bisec_left(a, 4)  bisect_right(a, 4)

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))

실행 결과
2
4

#값이 특정 범위에 속하는 데이터 개수 구하기

from bisect import bisect_left, bisect_right

#값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
  right_index = bisec_right(a, right_value)
  left_index = bisec_left(a, left_value)
  return right_index - left_index

#배열 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

#값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

#값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))

#파라메트릭 서치(Parametric Search)
#파라메트릭 서치란 최적화 문제를 결정 문제('예' 혹은 '아니오')로 바꾸어 해결하는 기법임
# 예시:특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
#일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 이진 탐색을 이용하여 해결할 수 있음

<문제>떡볶이 떡 만들기:문제 설명
#오늘 동빈이는 여행가신 부모님을 대신해서 떡집 일을 하기로 했습니다.
#오늘은 떡볶이 떡을 만드는 날입니다. 동빈이네 떡볶이 떡은 재밌게도 떡볶이 떡의 길이가 일정하지 않습니다.
#대신에 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰줍니다.
#절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단합니다. 높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고,
#낮은 떡은 잘리지 않습니다.
#예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면 자른 뒤 떡의 높이는
#15, 14, 10, 15cm각 될 것입니다. 잘린 떡의 길이는 차례대로 4, 0, 0, 2cm입니다.
#손님은 6cm 만큼의 길이를 가져갑니다.
#손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최대값을
#구하는 프로그램을 작성하세요.



