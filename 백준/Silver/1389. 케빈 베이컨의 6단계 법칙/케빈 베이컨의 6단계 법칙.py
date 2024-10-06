import sys
input = sys.stdin.readline

INF = int(1e9)

N, M = map(int, input().split())
graph = [[INF] * (N+1) for _ in range(N+1)]

# 자기 자신 0으로 초기화
for a in range(1, N+1):
    for b in range(1, N+1):
        if a == b :
            graph[a][b] = 0

# 입력 받기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 플로이드 워셜
for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 케빈 베이컨 구하기
answer = 0
min_num = INF
for a in range(1, N+1):
    temp = 0
    for b in range(1, N+1):
        temp += graph[a][b]
    
    if temp < min_num :
        min_num = min(temp, min_num)
        answer = a

print(answer)