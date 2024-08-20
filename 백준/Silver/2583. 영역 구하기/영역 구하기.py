import sys
input = sys.stdin.readline
from collections import deque

M, N, K = map(int, input().split())

# 이차원 배열 만들기
field = [[0 for _ in range(N)] for _ in range(M)]
for _ in range(K):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(M - ry, M - ly):
        for j in range(lx, rx):
            field[i][j] = 1

# bfs
move = [[1, 0], [0, -1], [-1, 0], [0, 1]]

def bfs(startX, startY):
    size = 1
    queue = deque([[startX,startY]])

    while queue:
        x, y = queue.popleft()

        field[y][x] = 1
        for m in move :
            X = m[0] + x
            Y = m[1] + y
            if(0 <= X < N and 0 <= Y < M) and field[Y][X] == 0 :
                queue.append([X, Y])
                field[Y][X] = 1 
                size += 1
    return size


cnt = 0
sizes = []
for i in range(M):
    for j in range(N):
        if field[i][j] == 0 :
            size = bfs(j, i)
            cnt += 1
            sizes.append(size)

sizes.sort()
print(cnt)
print(*sizes, sep="\n")