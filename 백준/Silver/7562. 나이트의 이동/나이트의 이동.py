import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
moves = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]

for _ in range(T):
    N = int(input()) # 한 변의 길이
    sx, sy = map(int, input().split()) # 시작 좌표
    ex, ey = map(int, input().split()) # 끝 좌표

    queue = deque([[sx, sy, 0]]) # 시작 x, 시작 y, 카운트
    visited = [[0 for _ in range(N)] for _ in range(N)]

    while queue:
        x, y, c = queue.popleft()

        if x == ex and y == ey :
            print(c)
            break
        
        for m in moves:
            X = x + m[0]
            Y = y + m[1]

            if X < 0 or X >= N or Y < 0 or Y >= N or visited[X][Y] > 0 :
                continue
            
            queue.append([X, Y, c+1])
            visited[X][Y] += 1