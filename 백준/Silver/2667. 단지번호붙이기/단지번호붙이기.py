from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

# 1) 이차원 배열 만들기
field = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    str = list(input())
    for j in range(N):
        if str[j] == '1':
            field[i][j] = 1

cnt = 0
lst = []

# 2) bfs
def bfs(startX, startY):
    house = 0
    queue = deque([[startX, startY]])
    while queue:
        x, y = queue.popleft()
        field[y][x] = 0
        house += 1
        moveX = [1, -1]
        moveY = [-1, 1]

        for mx in moveX:
            X = mx + x
            if (0 <= X < N) and field[y][X] == 1 :
                queue.append([X, y])
                field[y][X] = 0

        
        for my in moveY:
            Y = my + y
            if(0 <= Y < N) and field[Y][x] == 1 :
                queue.append([x, Y])
                field[Y][x] = 0
    lst.append(house)

for i in range(N):
    for j in range(N):
        if field[i][j] == 1 :
            bfs(j, i)
            cnt += 1

print(cnt)
lst.sort()
print(*lst, sep="\n")