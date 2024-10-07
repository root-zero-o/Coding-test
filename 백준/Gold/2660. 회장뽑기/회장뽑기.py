import sys
input = sys.stdin.readline

INF = int(1e9)
N = int(input())
graph = [[INF] * (N+1) for _ in range(N+1)]

for a in range(1, N+1):
    for b in range(1, N+1):
        if a == b :
            graph[a][b] = 0

while True :
    a, b = map(int, input().split())
    if a == -1 :
        break

    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

min_num = []
min_score = INF

for a in range(1, N+1):
    temp = 0
    for b in range(1, N+1):
        temp = max(temp, graph[a][b])
    
    if temp < min_score:
        min_num = [a]
        min_score = temp
    elif temp == min_score:
        min_num.append(a)
    
print(min_score, len(min_num))
print(*min_num)