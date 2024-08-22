import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)
from collections import deque

# 이차원 배열 만들기
N, M = map(int, input().split())

field = []
for _ in range(N):
    field.append(list(map(int, input().split())))

move = [[1, 0], [0, -1], [-1, 0], [0, 1]]

# dfs 정의
def dfs(x, y):
    global size

    field[y][x] = 0
    size += 1
    for m in move :
        X = m[0] + x
        Y = m[1] + y
        if X < 0 or Y < 0 or X >= M or Y >= N : continue
        elif field[Y][X] == 1 :
            dfs(X, Y)
    return size


# bfs 정의
def bfs(startX, startY):
    global maxSize
    queue = deque([[startX, startY, 1]])

    field[startY][startX] = 0

    while queue:
        x, y, size = queue.popleft()

        for m in move :
            X = m[0] + x
            Y = m[1] + y

            if X < 0 or Y < 0 or X >= M or Y >= N : continue
            elif field[Y][X] == 1 :
                field[Y][X] = 0
                queue.append([X, Y, size+1])
                maxSize = max(maxSize, size+1)

# (0,0)부터 탐색하며 최댓값, 갯수 카운트
cnt = 0
maxSize = 0
for i in range(N):
    for j in range(M):
        if field[i][j] == 1 :
            size = 0
            maxSize = max(maxSize, dfs(j, i))
            cnt += 1

print(cnt)
print(maxSize)