from collections import deque
import sys
input = sys.stdin.readline

T = int(input())    

for _ in range(T):
    H, W = map(int, input().split())
    # 이차원 배열 만들기
    field = [['.' for _ in range(W)] for _ in range(H)]

    for i in range(H):
        str = list(input())
        for j in range(W):
            if str[j] == '#' :
                field[i][j] = '#'
    # bfs
    cnt = 0

    def bfs(startX, startY):
        queue = deque([[startX, startY]])
        while queue :
            x, y = queue.popleft()
            field[y][x] = '.'
            move = [[1, 0], [0, -1], [-1, 0], [0, 1]]

            for m in move :
                X = m[0] + x
                Y = m[1] + y
                if (0 <= X < W and 0 <= Y < H) and field[Y][X] == '#':
                    queue.append([X, Y])
                    field[Y][X] = '.'
    
    for i in range(H):
        for j in range(W):
            if field[i][j] == '#':
                bfs(j, i)
                cnt += 1
            
    print(cnt)