import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    distance = [INF for _ in range(N+1)] 
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])
    return distance

a = dijkstra(1) # 1부터 N까지
b = dijkstra(v1) # v1부터 N까지
c = dijkstra(v2) # v2부터 N까지

answer = min(a[v1] + b[v2] + c[N], a[v2] +  c[v1] + b[N])

if answer >= INF:
    print(-1)
else:
    print(answer)