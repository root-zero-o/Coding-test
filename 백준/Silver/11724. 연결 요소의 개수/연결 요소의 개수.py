import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())

# 1) 인접 리스트 만들기
lst = [[] for _ in range(N+1)]
for i in range(M):
    start, end = map(int, input().split())
    lst[start].append(end)
    lst[end].append(start)

# 2) 방문 노드 저장
visited = [0] * (N+1)

# 3) dfs 
def dfs(start):
    visited[start] = 1
    for v in lst[start]:
        if not visited[v]:
            dfs(v)

# 4) count
cnt = 0
for i in range(1,N+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)