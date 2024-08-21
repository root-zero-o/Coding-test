import sys
input = sys.stdin.readline
from collections import deque

# 이차원 배열 만들기
H, W = map(int, input().split())

field = []
for i in range(H):
    field.append(list(input().strip('\n')))

move = [[1, 0], [0, -1], [-1, 0], [0, 1]]

# bfs 정의
def bfs(startX, startY):
    maxDis = 0
    queue = deque([[startX, startY, 1]])

    visited = [[0 for _ in range(W)] for _ in range(H)]
    visited[startY][startX] = 1

    while queue:
        x, y, dis = queue.popleft()

        for m in move :
            X = m[0] + x
            Y = m[1] + y

            if X < 0 or Y < 0 or X >= W or Y >= H : continue
            elif field[Y][X] == 'L' and (visited[Y][X] == 0 or visited[Y][X] > dis+1):
                maxDis = max(maxDis, dis+1)
                visited[Y][X] = 1
                queue.append([X, Y, dis+1])
    return maxDis
    
# (0,0)부터 시작해 걸리는 시간의 최댓값 찾기
answer = 0
for i in range(H):
    for j in range(W):
        if field[i][j] == 'L':
            answer = max(answer, bfs(j, i))

print(answer-1)