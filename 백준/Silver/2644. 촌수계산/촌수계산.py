# N, M = map(int, input().split())
# lst = list(map(int, input().split()))

# 재귀함수 쓸 때 필수
import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input()) # 노드의 수
start, end = map(int, input().split())
M = int(input()) # 간선의 수

# 1) 인접 리스트 만들기
lst = [[] for _ in range(N+1)]
for i in range(M):
    x, y = map(int, input().split())
    lst[x].append(y)
    lst[y].append(x)

# 2) 방문 노드 저장
visited = [-1] * (N+1)

queue = deque([[start, 0]])

visited[start] = 0
while queue:
    v, dis = queue.popleft()

    for j in lst[v]:
        if visited[j] == -1 or visited[j] > dis+1:
            queue.append([j, dis+1])
            visited[j] = dis+1


print(visited[end])
