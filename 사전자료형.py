#사전 자료형

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

data1 = {
  '사과':'Apple',
  '바나나':'Banana',
  '코코넛':'Coconut'
}

print(data)
print(data1)
if '사과' in data:
  print("'사과'를 키로 가지는 데이터가 존재합니다.")

#키 데이터만 담은 리스트
key_list = data.keys()

#값 데이터만 담은 리스트
value_list = data.values()

print(key_list)
print(value_list)

#각 키에 따른 값을 하나씩 출력
for key in key_list:
  print(data[key])
  
data1_key_list = list(data1.keys())
print(data1_key_list)

#집합 자료형
# 중복을 허용하지 않음
# 순서가 없음
#집합은 리스트 혹은 문자열을 이용해서 초기화할 수 있음.
# 이때 set() 함수를 이용함
#혹은 중괄호({}) 안에 각 원소를 콤마(,)를 기준으로 구분하여 삽입함으로써 초기화할 수 있음
#데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있음

#집합 자료형 초기화 방법1
data = set([1, 1, 2, 3, 4, 4, 5])

#집합 자료형 초기화 방법2
data = {1, 1, 2, 3, 4, 4, 5}
print(data)

#집합 자료형의 연산 : 합집합, 교집합, 차집합

a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

#합집합
print(a | b)

#교집합
print(a & b)

#차집합
print(a - b)

data = set([1, 2, 3])
print(data)

#새로운 원소 추가
data.add(4)
print(data)

#새로운 원소 여러 개 추가
data.update([5, 6])
print(data)

#특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)

#사전 자료형과 집합 자료형의 특징
#리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있음
#사전 자료형과 집합 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없음
# 사전의 키(Key) 혹은 집합의 원소(Element)를 이용해 O(1)의 시간 복잡도로 조회함
