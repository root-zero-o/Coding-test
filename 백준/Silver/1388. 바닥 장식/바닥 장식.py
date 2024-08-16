N, M = map(int, input().split())

# 1) 이차원 배열 만들기
lst = [[] for _ in range(N)]
for i in range(N):
    temp = input()
    for j in range(M):
        lst[i].append(temp[j])

# 2) dfs
def dfs(x, y):

    # 2-1) 바닥 장식 모양이 '-'일 때
    if lst[x][y] == '-':
        lst[x][y] = 1 # 방문 처리
        for _y in [1, -1]: # 좌우 확인
            Y = y + _y
            if(Y > 0 and Y < M) and lst[x][Y] == '-':
                dfs(x, Y)

    # 2-2) 바닥 장식 모양이 '|'일 때
    if lst[x][y] == '|':
        lst[x][y] = 1 # 방문 처리
        for _x in [1, -1]: # 상하 확인
            X = x + _x
            if(X > 0 and X < N) and lst[X][y] == '|':
                dfs(X, y)

# 3) 카운트
cnt = 0
for i in range(N):
    for j in range(M):
        if lst[i][j]  == '-' or lst[i][j] == '|':
            dfs(i, j)
            cnt += 1

print(cnt)