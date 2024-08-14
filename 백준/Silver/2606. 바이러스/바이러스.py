N = int(input()) # N개의 노드(1~N)
M = int(input()) # M개의 간선

# 1) 인접 리스트 만들기
lst = [[] for _ in range(N+1)]
for i in range(M):
    start, end = map(int, input().split())
    lst[start].append(end)
    lst[end].append(start)

# 2) 방문했던 노드 저장할 리스트
visited = [0] * (N+1)

# 3) dfs
def dfs(v):
    visited[v] = 1
    for i in lst[v]:
        if visited[i] == 0:
            dfs(i)

dfs(1)

print(sum(visited) - 1)