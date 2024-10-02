import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
moves = [[1, 0], [0, -1], [-1, 0], [0, 1]]
cnt = 1
while True :
    N = int(input())

    if not N : break

    cave = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        cave.append(temp)
    
    distance = [[INF for _ in range(N)] for _ in range(N)]

    q = []
    heapq.heappush(q, [cave[0][0], 0, 0])
    distance[0][0] = cave[0][0]

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[y][x] < dist :
            continue

        for m in moves:
            X = x + m[0]
            Y = y + m[1]

            if X >= N or X < 0 or Y >= N or Y < 0 : continue

            cost = dist + cave[Y][X]
            if cost < distance[Y][X]:
                distance[Y][X] = cost
                heapq.heappush(q, [cost, X, Y])
    
    print(f"Problem {cnt}: {distance[N-1][N-1]}")
    cnt += 1