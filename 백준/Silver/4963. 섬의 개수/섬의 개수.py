import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

while True:
    W, H = map(int, input().split())
    if(W == 0 and H == 0): break

    # 1) 이차원 배열 만들기
    lst = []
    for i in range(H):
        lst.append(list(map(int, input().split())))

    # 2) dfs 선언
    def dfs(x, y):
        lst[y][x] = 0 # 방문 처리

        # 상하좌우+대각선으로 움직일 방향
        move = [[0,1], [1,1], [1,0],[1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

        for m in move :
            X = m[0] + x
            Y = m[1] + y

            if(X >= 0 and X < W) and (Y >=0 and Y < H) and lst[Y][X] == 1 :
                dfs(X, Y)

    # 3) 카운트
    cnt = 0
    for i in range(H):
        for j in range(W):
            if lst[i][j] == 1:
                dfs(j, i)
                cnt += 1

    print(cnt)