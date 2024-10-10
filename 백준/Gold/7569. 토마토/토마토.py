import sys
from collections import deque
input = sys.stdin.readline
moves = [[1, 0 ,0],[0, -1 , 0], [-1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, -1]]

N, M, H = map(int, input().split())
tomatoes =  [[list(map(int, input().split())) for _ in range(M)] for _ in range(H)]
queue = deque()

def bfs():
    while queue:
        x, y, z = queue.popleft()
        for m in moves :
            X = x + m[0]
            Y = y + m[1]
            Z = z + m[2]

            if X < 0 or X >= N or Y < 0 or Y >= M or Z < 0 or Z >= H : 
                continue

            if tomatoes[Z][Y][X] == 0 :
                tomatoes[Z][Y][X] = tomatoes[z][y][x] + 1
                queue.append([X, Y, Z])

for a in range(H):
    for b in range(M):
        for c in range(N):
            if tomatoes[a][b][c] == 1 :
                queue.append([c, b, a])

bfs()
answer = 0

for a in range(H):
    for b in range(M):
        for c in range(N):
            if tomatoes[a][b][c] == 0 :
                print(-1)
                exit(0)
            answer = max(answer, tomatoes[a][b][c])
print(answer - 1)
