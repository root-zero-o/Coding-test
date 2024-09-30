import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

# N : 노드 개수, M: 간선 개수, K: 최단거리, X: 출발점
N, M, K, X = map(int, input().split())
distance = [INF] * (N+1)
lst = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    # 단방향
    lst[start].append(end)

def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0
    while q :
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in lst[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, [cost, i])

dijkstra(X)
    
answer = []
for i in range(1, N+1):
    if distance[i] == K :
        answer.append(i)

answer.sort()
if len(answer):
    for i in answer:
        print(i)
else:
    print(-1)