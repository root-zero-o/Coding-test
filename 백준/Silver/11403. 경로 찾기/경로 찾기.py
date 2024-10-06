import sys
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    temp = list(map(int, input().split()))
    graph.append(temp)

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for i in range(N):
    print(*graph[i])