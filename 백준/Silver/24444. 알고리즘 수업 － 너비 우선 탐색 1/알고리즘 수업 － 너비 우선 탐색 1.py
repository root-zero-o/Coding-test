import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M, R = map(int, input().split())

# 인접 리스트 만들기
lst = [[] for _ in range(N+1)]
for i in range(M):
    start, end = map(int, input().split())
    lst[start].append(end)
    lst[end].append(start)

for i in lst:
    i.sort()

# 방문 노드 저장
visited = [0] * (N+1)

# bfs
cnt = 1
def bfs(start):
    global cnt
    queue = deque([start])
    visited[start] = cnt
    while queue:
        v = queue.popleft()
        for i in lst[v]:
            if not visited[i]:
                cnt += 1
                queue.append(i)
                visited[i] = cnt

bfs(R)
for i in range(1, N+1):
    print(visited[i])