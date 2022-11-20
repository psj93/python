x = 15
if x >= 10:
  print("x >= 10")

if x >= 0:
  print("x >= 0")

if x >= 30:
  print("x >= 30")

#파이썬에서는 코드의 블록(Block)을 들여쓰기(Indent)로 지정함
#파이썬 스타일 가이드라인에서는 4개의 공백 문자를 사용하는 것을 표준으로 설정하고 있음

#조건문의 기본 형태
#if ~ elif ~ else
# 조건문을 사용할 때 elif 혹은 else 부분은 경우에 따라서 사용하지 않아도 됨

if 조건문 1:
  조건문이 1이 True일 때 실행되는 코드
elif 조건문 2:
  조건문 1에 해당하지 않고, 조건문 2가 True일 때 실행되는 코드
else:
  위의 모든 조건문이 모두 True 값이 아닐 때 실행되는 코드

score = 85

if score >= 90:
  print("학점:A")
elif score >= 80:
  print("학점:B")
elif score >= 70:
  print("학점:C")
else:
  print("학점:F")

#비교 연산자
# X == Y, X != Y, X > Y, X < Y, X >= Y, X <= Y

#논리 연산자
# X and Y, X or Y, not X

a = 15

if a <= 20 and a >= 0:
  print("Yes")

#기타 연산자
#x in 리스트 : 리스트 안에 x가 들어가 있을 때 True임
#x not in 문자열 : 문자열 안에 x가 들어가 있지 않을 때 True임
#리스트, 튜플, 문자열, 딕셔너리 모두에서 사용이 가능함

#pass 키워드
#아무것도 처리하고 싶지 않을 때 pass 키워드 사용함
#예) 디버깅 과정에서 일단 조건문의 형태만 만들어 놓고 조건문을 처리하는 부분은 비워놓고 싶은 경우

score = 85
if score >= 80:
  pass #나중에 작성할 소스코드
else:
  print('성적이 80점 미만입니다.')
  
print('프로그램을 종료합니다.')

#조건문의 간소화
#조건문에서 실행될 소스코드가 한 줄인 경우, 굳이 줄 바꿈을 하지 않고도 간략하게 표현할 수 있음

score = 85
if score >= 80: result = "Success"
else: result = "Fail"

#조건부 표현식은 if ~ else 문을 한 줄에 작성할 수 있도록 해줌

score = 85
result = "Success" if score >= 80 else "Fail"
print(result)

#조건문 내에서의 부등식
#조건문 안에서 수학의 부등식을 그대로 사용할 수 있음
#예) x > 0 and x < 20과 0 < x < 20은 같은 결과를 반환함

#코드 스타일 1
x = 15
if x > 0 and x < 20:
  print("x는 0 이상 20 미만의 수입니다.")

#코드 스타일 2
x = 15
if 0 < x < 20:
  print("x는 0 이상 20 미만의 수입니다.")
