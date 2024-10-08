import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())
graph = [[INF] * (N+1) for _ in range(N+1)]
history = [[[i] for i in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            if a == b : continue
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                history[a][b] = history[a][k] + history[k][b]

for a in range(1, N+1):
    for b in range(1, N+1):
        if graph[a][b] == INF :
            print(0, end=" ")
        else :
            print(graph[a][b], end=" ")
    print()

for i in range(1,N+1):
  for j in range(1,N+1):
    if graph[i][j] == INF:
      print(0)
    else:
        print(len(history[i][j])+1,i,*history[i][j])