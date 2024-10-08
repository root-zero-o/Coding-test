import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
graph = [[INF] * (N+1) for _ in range(N+1)]

for a in range(1, N+1):
    for b in range(1, N+1):
        if a == b :
            graph[a][b] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = [INF] + []
for i in range(1, N+1):
    temp = INF
    for j in range(1, N+1):
        if i == j : 
            continue
        temp = min(temp, graph[i][j] + graph[j][i])
    distance.append(temp)

answer = min(distance)
if answer == INF:
    print(-1)
else :
    print(answer)