import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수
graph = [[] for _ in range(N+1)] # 버스 경로
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split()) # 출발점, 도착점
distance = [INF] * (N+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0

    while q :
        dist, now = heapq.heappop(q)
        if now == end :
            break
        if distance[now] < dist :
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])

dijkstra(start)
print(distance[end])