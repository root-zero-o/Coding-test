from collections import deque
import sys
input = sys.stdin.readline

N = int(input())    

# 이차원 배열
field = []
for i in range(N):
    field.append(list(map(int, input().split())))
rain_max = max(map(max, field))

# bfs
def bfs(startX, startY, rain) :
    queue = deque([[startX, startY]])
    
    while queue:
        x, y = queue.popleft()
        move = [[1, 0], [0, -1], [-1, 0], [0, 1]]

        for m in move:
            X = m[0] + x
            Y = m[1] + y

            if(0 <= X < N and 0 <= Y < N) and (sink[Y][X] == 0 and field[Y][X] > rain):
                queue.append([X, Y])
                sink[Y][X] = 1

max = 0
for r in range(rain_max):
    sink = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if sink[i][j] == 0 and field[i][j] > r :
                bfs(j, i, r)
                cnt += 1

    if cnt > max :
        max = cnt

print(max)