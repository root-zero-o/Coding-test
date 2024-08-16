import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M, R = map(int, input().split())

# dfs
def dfs(start):
    global cnt
    visited[start] = cnt
    for v in lst[start]:
        if not visited[v]:
            cnt += 1
            dfs(v)

# 인접 리스트 만들기
lst = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 1

for i in range(M):
    start, end = map(int, input().split())
    lst[start].append(end)
    lst[end].append(start)

for i in lst:
    i.sort()

dfs(R)
for i in range(1, N+1):
    print(visited[i])
