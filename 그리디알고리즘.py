#그리디 알고리즘(탐욕법)은 현재 상황에서 지금 당장 좋은 것만 고르는 방법을 의미함
#그리디 해법은 그 정당성 분석이 중요함
# 단순히 가장 좋아 보이는 것을 반복적으로 선택해도 최적의 해를 구할 수 있는지 검토
#일반적인 상황에서 그리디 알고리즘은 최적의 해를 보장할 수 없을 때가 많음
#하지만 코딩 테스트에서의 대부분의 그리디 문제는 탐욕법으로 얻은 해가 최적의 해가 되는 상황에서 이를 추론할 수 있어야 풀리도록 출제됨

<문제> 거스름 돈:문제 설명
당신은 음식점의 계산을 도와주는 점원입니다.
카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전히 무한히 존재한다고 가정합니다.
손님에게 거슬러 주어야할 돈이 N원일때 거슬러 주어야 할 동전의 최소 개수를 구하세요.
단, 거슬러 줘야 할 돈 N은 항상 10의 배수입니다.

<문제> 거스름 돈:문제 해결 아이디어
최적의 해를 빠르게 구하기 위해서는 가장 큰 화폐 단위부터 돈을 거슬러 주면 됨.
N원을 거슬러줘야 할 때, 가장 먼저 500원으로 거슬러 줄 수 있을 만큼 거슬러 줌.
이후에 100원, 50원, 10원짜리 동전을 차례대로 거슬러 줄 수 있을 만큼 거슬러 주면 됨.
N = 1,260일 때의 예시를 확인해 봅시다.

500원 : 2
100원 : 2
50원 : 1
10원 : 1

<문제> 거스름 돈:정당성 분석
가장 큰 화폐 단위부터 돈을 거슬러 주는 것이 최적의 해를 보장하는 이유는 무엇일까요?
 가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올 수 없기 때문임

n = 1260
count = 0

#큰 단위의 화폐부터 차례대로 확인하기
array = [500, 100, 50, 10]

for coin in array:
  count += n // coin #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
  n %= coin

print(count)

<문제>1이 될때까지:문제 설명
어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 합니다.
단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있습니다.
 1. N에서 1을 뺍니다.
 2. N을 K로 나눕니다.
예를 들어 N이 17, K가 4라고 가정합시다. 이때 1번의 과정을 한번 수행하면 N은 16이 됩니다.
이후에 2번의 과정을 두 번 수행하면 N은 1이 됩니다. 결과적으로 이 경우 전체 과정을 실행한 횟수는 3이 됩니다.
이는 N을 1로 만드는 최소 횟수입니다.
N과 K가 주어질 때 N이 1이 될때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하세요.

입력 조건 : 첫째 줄에 N(1 <= N <= 100,000)과 K(2 <= K <= 100,000)가 공백을 기준으로 하여 각각 자연수로 주어짐
출력 조건 : 첫째 줄에 N이 1일 될때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최소값을 출력합니다.

입력 예시 : 25 5
출력 예시 : 1
 
<문제>1이 될때까지:문제 해결 아이디어
주어진 N에 대해 최대한 많이 나누기를 수행하면 됨
N의 값을 줄일 때 2 이상의 수로 나누는 작업이 1을 빼는 작업보다 수를 훨씬 많이 줄일 수 있음

<문제>1이 될때까지:정당성 분석
가능하면 최대한 많이 나누느 작업이 최적의 해를 보장할 수 있을까요?
N이 아무리 큰 수여도, K로 계속 나눈다면 기하급수적으로 빠르게 줄일 수 있음.
다시 말해 K가 2 이상이기만 하면, K로 나누는 것이 1을 빼는 것보다 항상 빠르게 N을 줄일 수 있음
또한 N은 항상 1에 도달하게 됨(최적의 해 성립)

<문제>1이 될때까지:답안 예시
 
#N, K를 공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())

result = 0

while True:
 #N이 K로 나누어 떨어지는 수가 될 때까지 빼기
 target = (n // k) * k
 result += n - target
 n = target
 
 #N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
 if n < k:
  break;
 
 #K로 나누기
 result += 1
 n //= k
 
#마지막으로 남은 수에 대해 1씩 빼기
result += (n - 1)
print(result)
 
<문제>곱하기 혹은 더하기:문제 설명
각 자리가 숫자(0부터 9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에
'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요.
단, +보다 x를 먼저 계산하는 일반적일 방식과는 달리, 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정합니다.
예를 들어 02984라는 문자열로 만들 수 있는 가장 큰 수는 ((((0 + 2) x 9) x 8) x 4) = 576입니다. 또한 만들어질 수 있는
가장 큰 수는 항상 20억 이하의 정수가 되도록 입력이 주어집니다.

입력 조건 : 첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 S가 주어집니다.(1 <= S의 길이 <= 20)
출력 조건 : 첫째 줄에 만들어질 수 있는 가장 큰 수를 출력합니다.
입력 예시1 : 02984
출력 예시1 : 576
입력 예시2 : 567
출력 예시2 : 210
 
<문제>곱하기 혹은 더하기:문제 해결 아이디어
대부분의 경우 '+' 보다는 'x'가 더 값을 크게 만듬
다만 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기를 수행하는 것이 효율적임
따라서 두 수에 대하여 연산을 수행할 때, 두 수 중에서 하나라도 1 이하인 경우에는 더하며, 두 수가
모두 2 이상인 경우에는 곱하면 정답임

<문제>곱하기 혹은 더하기:답안 예시

data = input()

#첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
 #두 수 중에서 하나라도 '0' 또는 '1'인 경우, 곱하기보다는 더하기 수행
 num = int(data[i])
 if num <= 1 or result <= 1:
  result += num
 else:
  result *= num

print(result)

<문제>모험가 길드:문제 설명
한 마을에 모험가가 N명 있습니다. 모험가 길드에서는 N명의 모험가를 대상으로 '공포도'를 측정했는데,
'공포도'가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어집니다.
모험가 길드장인 동빈이는 모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는 반드시 X명 이상으로
구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정했습니다.
동빈이는 최대 몇 개의 모험가 그룹을 만들 수 있는지 궁금합니다. N명의 모험가에 대한 정보가 주어졌을 때,
여행을 떠날 수 있는 그룹의 최대값을 구하는 프로그램을 작성하세요.

예를 들어 N=5이고, 각 모험가의 공포도가 다음과 같다고 가정합시다.
2 3 1 2 2
이 경우 그룹 1에 공포도가 1,2,3인 모험가를 한명씩 넣고, 그룹 2에 공포도가 2인 남은 두 명을 넣게 되면
총 2개의 그룹을 만들 수 있습니다.
또한 몇 명의 모험가는 마을에 그대로 남아 있어도 되기 때문에, 모든 모험가를 특정한 그룹에 넣을 필요는
없습니다.

<문제>모험가 길드:문제 조건
입력 조건 : 첫째 줄에 모험가의 수 N이 주어집니다.(1 <= N <= 100,000)
           둘째 줄에 각 모험가의 공포도의 값을 N 이하의 자연수로 주어지며, 각 자연수는 공백으로 구분합니다.
출력 조건 : 여행을 떠날 수 있는 그룹 수의 최대값을 출력합니다.
입력 예시 : 5
           2 3 1 2 2
출력 예시 : 2

<문제>모험가 길드:문제 해결 아이디어
오름차순 정렬 이후에 공포도가 가장 낮은 모험가부터 하나씩 확인함

2 2 1 2 2
1 2 2 2 3

앞에서부터 공포도를 하나씩 확인하며 '현재 그룹에 포함된 모험가의 수'가 현재 확인하고 있는 공포도'보다 크거나 같다면
이를 그룹으로 설정하면 됨

  1      2  2      2 3
 그룹1   그룹2

이러한 방법을 이용하면 공포도가 오름차순으로 정렬되어 있다는 점에서, 항상 최소한의 모험가의 수만 포함하여 그룹을 결성하게 됨

<문제>모험가 길드:답안 예시

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 #총 그룹의 수
count = 0 #현재 그룹에 포함된 모험가의 수

for i in data: #공포도를 낮은 것부터 하나씩 확인
 count += 1 #현재 그룹에 해당 모험가를 포함시키기
 if count >= i: #현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
  result += 1 #총 그룹의 수 증가시키기
  count = 0 #현재 그룹에 포함된 모험가의 수 초기화

print(result) #총 그룹의 수 출력
