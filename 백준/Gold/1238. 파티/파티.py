import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start, end):
    q = []
    heapq.heappush(q, [0, start])
    distance = [INF] * (N+1)
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
 
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])
    return distance[end]

answer = []
for i in range(1, N+1):
    temp1 = dijkstra(i, X)
    temp2 = dijkstra(X, i)
    answer.append(temp1 + temp2)

print(max(answer))