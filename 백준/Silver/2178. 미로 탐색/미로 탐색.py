from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 이차원 배열 만들기
field = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    str = list(input())
    for j in range(M):
        if str[j] == '1':
            field[i][j] = 1

# bfs
queue = deque([[0, 0, 0]])

while queue:
    x, y, dis = queue.popleft()
    field[y][x] = dis+1
    move = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    for m in move:
        X = m[0] + x
        Y = m[1] + y
        if(0 <= X < M and 0 <= Y < N) and (field[Y][X] == 1 or field[Y][X] > dis+1):
            queue.append([X, Y, dis+1])
            field[Y][X] = dis+1

print(field[N-1][M-1])