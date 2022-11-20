#함수 종류
# 내장 함수 : 파이썬이 기본적으로 제공하는 함수
# 사용자 정의 함수 : 개발자가 직접 정의하여 사용할 수 있는 함수

def 함수명(매개변수):
  실행할 소스코드
  return 반환 값

#더하기 함수 예시 1

def add(a, b):
  return a + b

print(add(3, 7))

#더하기 함수 예시 2

def add(a, b):
  print('함수의 결과:', a + b)
  
add(3, 7)

#파라미터 지정하기
#파라미터의 변수를 직접 지정할 수 있음
# 이 경우 매개변수의 순서가 달라도 상관 없음

def add(a, b):
  print('함수의 결과:', a + b)
  
add(b = 3, a = 7)

#global 키워드
#global 키워드로 변수를 지정하면 해당 함수에서는 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조하게 됨

a= 0

def func():
  global a
  a += 1
  
for i in range(10):
  func()
  
print(a)

#여러 개의 반환 값
#파이썬에서 함수는 여러 개의 반환 값을 가질 수 있음

def operator(a, b):
  add_var = a + b
  subtract_var = a - b
  multiply_var = a * b
  divide_var = a / b
  return add_var, subtract_var, multiply_var, divide_var

a, b, c, d = operator(7, 3)
print(a, b, c, d)

#람다 표현식
#람다 표현식을 이용하면 함수를 간단하게 작성할 수 있음
# 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다는 점이 특징임

def add(a, b):
  return a + b

#일반적인 add() 메서드 사용
print(add(3, 7))

#람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a + b)(3, 7))

#람다 표현식 예시:내장 함수에서 자주 사용되는 람다 함수

array = [('홍길도', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
  return x[1]

print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))

#람다 표현식 예시:여러 개의 리스트에 적용

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a + b, list1, list2)
print(list(result))
