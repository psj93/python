#탐색이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 말함
#대표적인 그래프 탐색 알고리즘으로 DFS와 BFS가 있음
#DFS/BFS는 코딩 테스트에서 매우 자주 등장하는 유형이므로 반드시 숙지해야 함

#스택 자료구조
#먼저 들어온 데이터가 나중에 나가는 형식(선입후출)의 자료구조임
#입구와 출구가 동일한 형태로 스택을 시각화할 수 있음
#박스쌓기 예시

#스택 구현 예제
stack = []

#삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) #최상단 원소부터 출력
print(stack) #최하단 원소부터 출력

#큐 자료구조
#먼저 들어온 데이터가 먼저 나가는 형식(선입선출)의 자료구조임
#큐는 입구와 출구가 모두 뚫려있는 터널과 같은 형태로 시각화할 수 있음

#큐 동작 예제
from collections import deque

#큐 구현을 위해 deque 라이브러리 사용
queue = deque()

#삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) #먼저 들어온 순서대로 출력
queue.reverse() #역순으로 바꾸기
print(queue) #나중에 들어온 원소부터 출력

#재귀 함수
#자기 자신을 다시 호출하는 함수를 의미함
#단순한 형태의 재귀 함수 예제

def recursive_function():
  print('재귀 함수를 호출합니다.')
  recursive_function()
  
recursive_function()

#재귀 함수의 종료 조건
#재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야 함
#종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출될 수 있음
#종료 조건을 포함한 재귀 함수 예제

def recursive_function(i):
  #100번째 호출을 했을 때 종료되도록 종료 조건 명시
  if i == 100:
    return
  print(i,'번째 재귀 함수에서', i + 1, '번째 재귀함수를 호출합니다.')
  recursive_function(i + 1)
  print(i, '번째 재귀 함수를 종료합니다.')
  
recursive_function(1)

#팩토리얼 구현 예제
#n! = 1 x 2 x 3 x ... x (n - 1) x n

#반복적으로 구현한 n!
def factorial_iterative(n):
  result = 1
  #1부터 n까지의 수를 차례대로 곱하기
  for i in range(1, n + 1):
    result *= i
  return result

#재귀적으로 구현한 n!
def factorial_recursive(n):
  if n <= 1: #n이 1 이하인 경우 1을 반환
    return 1
  
  #n! = n * (n - 1)!를 그대로 코드로 작성하기
  return n * factorial_recursive(n - 1)

#각각의 방식으로 구현한 n! 출력(n = 5)
print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))

#최대공약수 계산(유클리드 호제법) 예제
#두 개의 자연수에 대한 최대 공약수를 구하는 대표적인 알고리즘으로는 유클리드 호제법이 있음
#유클리드 호제법
# 두 자연수 A, B에 대해(A > B) A를 B로 나눈 나머지를 R이라고 합시다.
# 이때 A와 B의 최대 공약수는 B와 R의 최대 공약수와 같습니다.
#유클리드 호제법의 아이디어를 그대로 재귀 함수로 작성할 수 있습니다.
# 예시 : GCD(192, 162)

 단계         A             B
  1          192           162
  2          162           30
  3          30            12
  4          12            6

def gcd(a, b):
  if a % b == 0:
    return b
  else:
    return gcd(b, a % b)

print(gcd(192,162))

#재귀 함수 사용의 유의 사항
#재귀 함수를 잘 활용하면 복잡한 알고리즘을 간결하게 작성할 수 있음
# 단, 오히려 다른 사람이 이해하기 어려운 형태의 코드가 될 수도 있으므로 신중하게 사용해야 함
#모든 재귀 함수는 반복문을 이용하여 동일한 기능을 구현할 수 있음
#재귀 함수가 반복문보다 유리한 경우도 있고 불리한 경우도 있음
#컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓임
# 그래서 스택을 사용해야 할 때 구현상 스택 라이브러리 대신에 재귀 함수를 이용하는 경우가 많음

#DFS(Depth-First Search)
#DFS는 깊이 우선 탐색이라고도 부르며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘임
#DFS는 스택 자료구조(혹은 재귀 함수)를 이용하며, 구체적인 동작 과정은 다음과 같음
# 1.탐색 시작 노드를 스택에 삽입하고 방문 처리함
# 2.스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리함
#   방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
# 3.더 이상 2번의 과정을 수행할 수 없을 때까지 반복함

#DFS 소스코드 예제

def dfs(graph, v, visited):
  #현재 노드를 방문 처리
  visited[v] = True
  print(v, end=' ')
  #현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)
      
#각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1,7]
]

#각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False] * 9

#정의된 DFS 함수 호출
dfs(graph, 1, visited)

#BFS(Breadth-First Search)
#BFS는 너비 우선 탐색이라고도 부르며, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘임
#BFS는 큐 자료구조를 이용하며, 구체적인 동작 과정은 다음과 같음
# 1.탐색 시작 노드를 큐에 삽입하고 방문 처리함
# 2.큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리함
# 3.더 이상 2번의 과정을 수행할 수 없을 때까지 반복함

#BFS 소스코드 예제

from collections import deque

#BFS 메소드 정의
def bfs(graph, start, visited):
  #큐 구현을 위해 deque 라이브러리 사용
  queue = deque([start])
  #현재 노드를 방문 처리
  visited[start] = True
  #큐각 빌때까지 반복
  while queue:
    #큐에서 하나의 원소를 뽑아 출력하기
    v = queue.popleft()
    print(v, end=' ')
    #아직 방문하지 않은 인접한 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
        
#각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1,7]
]

#각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False] * 9

#정의된 BFS 함수 호출
bfs(graph, 1, visited)

<문제>음료수 얼려 먹기:문제 설명
#N x M 크기의 얼음 틀이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다.
#구멍이 뚫려 있는 부분끼리 상,하,좌,우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주합니다.
#이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하세요.
#다음의 4 x 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성됩니다.

00110
00011
11111
00000

<문제>음료수 얼려 먹기:문제 조건
#입력 조건:첫번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어집니다.(1 <= N <= 1,000)
#         두번째 줄부터 N+1 번째 줄까지 얼음 틀의 형태가 주어집니다.
#         이때 구멍이 뚫려 있는 부분은 0, 그렇지 않은 부분은 1입니다.
#출력 조건:한번에 만들 수 있는 아이스크림의 개수를 출력합니다.
#입력 예시: 4 5
           00110
           00011
           11111
           00000
#출력 예시 : 3

<문제>음료수 얼려 먹기:문제 해결 아이디어
#이 문제는 DFS 혹은 BFS로 해결할 수 있습니다. 일단 앞에서 배운 대로 얼음을 얼릴 수 있는 공간이 상,하,좌,우로
#연결되어 있다고 표현할 수 있으므로 그래프 형태로 모델링할 수 있음

#DFS를 활용하는 알고리즘은 다음과 같음
# 1.특정한 지점의 주변 상,하,좌,우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문함
# 2.방문한 지점에서 다시 상,하,좌,우를 살펴보면서 방문을 진행하는 과정을 반복하면, 연결된 모든 지점을 방문할 수 있음
# 모든 노드에 대해 1~2번의 과정을 반복하며, 방문하지 않은 지점의 수를 카운트함

<문제>음료수 얼려 먹기:답안예시
  
#DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
  #주어진 범위를 벗어나는 경우에는 즉시 종료
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  #현재 노드를 아직 방문하지 않았다면
  if graph[x][y] == 0:
    #해당 노드 방문 처리
    graph[x][y] = 1
    
    #상,하,좌,우의 위치들도 모두 재귀적으로 호출
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)
    return True
  return False

#N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

#2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
  graph.append(list(map(int,input())))
 
#모든 노드(위치)에 대해 음료수 채우기
result = 0
for i in range(n):
  for j in range(m):
    #현재 위치에서 DFS 수행
    if dfs(i, j) == True:
      result += 1
      
print(result) #정답 출력

