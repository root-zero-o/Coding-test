import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
field = []
for i in range(M):
    temp = [int(x) for x in input().strip()]
    field.append(temp)
distance = [[INF for _ in range(N)] for _ in range(M)]

def dijkstra(startX, startY):
    q = []
    heapq.heappush(q, [0, startX, startY])
    distance[startY][startX] = 0

    while q :
        dist, x, y = heapq.heappop(q)

        if distance[y][x] < dist :
            continue

        for m in moves :
            X = x + m[0]
            Y = y + m[1]

            if X >= N or X < 0 or Y >= M or Y < 0 : continue
            if distance[Y][X] < dist :
                continue

            cost = dist + field[Y][X]

            if cost < distance[Y][X]:
                distance[Y][X] = cost
                heapq.heappush(q, [cost, X, Y])

dijkstra(0, 0)
print(distance[M-1][N-1])