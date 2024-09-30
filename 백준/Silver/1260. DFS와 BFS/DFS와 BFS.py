import sys
from collections import deque
input = sys.stdin.readline

# 인접 리스트
N, M, V = map(int, input().split())
lst = [[] for _ in range(N+1)]
for i in range(M):
    start, end = map(int, input().split())
    lst[start].append(end)
    lst[end].append(start)
for i in range(N+1):
    lst[i].sort()

# dfs
visited_d = [0] * (N+1)
def dfs(v):
    visited_d[v] = 1
    print(v, end=" ")
    for i in lst[v]:
        if not visited_d[i] :
            dfs(i)

# bfs
visited_b = [0] * (N+1)
def bfs(v):
    queue = deque([v])
    visited_b[v] = 1

    while queue:
        num = queue.popleft()
        print(num, end=" ")
        for i in lst[num]:
            if not visited_b[i]:
                queue.append(i)
                visited_b[i] = 1

dfs(V)
print()
bfs(V)