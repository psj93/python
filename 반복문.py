#1부터 9까지 모든 정수의 합 구하기 예제(while문)
i = 1
result = 0

#i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
  result += i
  i += 1
  
print(result)

#1부터 9까지 홀수의 합 구하기 예제(while문)
i = 1
result = 0

#i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
  if i % 2 == 1:
    result += i
  i += 1

print(result)

#반복문 : for 문
# 'in" 뒤에 오는 데이터(리스트, 튜플 등)에 포함되어 있는 원소를 첫 번째 인덱스부터 차례대로 하나씩 방문함

for 변수 in 리스트:
  실행할 소스코드
  
array = [9, 8, 7, 6, 5]
for x in array:
  print(x)
  
#for 문에서 연속적인 값을 차례대로 순회할 때는 range()를 주로 사용함
# 이때 range(시작 값, 끝 값 + 1) 형태로 사용함
# 인자를 하나만 넣으면 자동으로 시작 값은 0이 됨

result = 0
#i는 1부터 9까지의 모든 값을 순회
for i in range(1, 10):
  result += i
  
print(result)

#continue 키워드
#반복문에서 남은 코드의 실행을 건너뛰고, 다음 반복을 진행하고자 할 때 continue를 사용함
#1부터 9까지의 홀수의 합을 구할 때 다음과 같이 작성할 수 있음

result = 0
for i in range(1, 10):
  if i % 2 == 0:
    continue
  result += i

print(result)

#break 키워드
#반복문을 즉시 탈출하고자 할 때 break를 사용함
#1부터 5까지의 정수를 차례대로 출력하고자 할 때 다음과 같이 작성할 수 있음

i = 1
while True:
  print("현재 i의 값:", i)
  if i == 5:
    break
  i += 1

#학생들의 합격 여부 판단 예제1) 점수가 80점만 넘으면 합격

scores = [90, 85, 77, 65, 97]
for i in range(5):
  if scores[i] >= 80:
    print(i + 1, "번 학생은 합격입니다.")

#학생들의 합격 여부 판단 예제2) 특정 번호의 학생은 제외하기

scores = [90, 85, 77, 65, 97]
cheating_student_list = {2, 4} #부정행위 학생
for i in range(5):
  if i + 1 in cheating_student_list:
    continue
  if scores[i] >= 80:
    print(i + 1, "번 학생은 합격입니다.")

#중첩된 반복문 : 구구단 예제

for i in range(2, 10):
  for j in range(1, 10):
    print(i, "X", j, "=", i * j)
  print()
