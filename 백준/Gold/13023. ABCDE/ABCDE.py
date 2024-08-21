import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M = map(int, input().split())

# 인접 리스트
lst = [[] for _ in range(N)]
visited = [0] * (N)

for i in range(M):
    start, end = map(int, input().split())
    lst[start].append(end)
    lst[end].append(start)

# dfs
answer = 0
def dfs(start, depth):
    global answer

    visited[start] = 1

    if depth == 4 :
        answer = 1
        return

    for i in lst[start] :
        if visited[i] == 0 :
            dfs(i, depth+1)
    visited[start] = 0

for i in range(N):
    dfs(i, 0)
    if answer : break

print(answer)