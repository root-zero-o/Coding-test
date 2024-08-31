N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1

for h in range(N):
    for w in range(N):
        if not dp[h][w] : continue
        if h == N-1 and w == N-1 : break
        move = board[h][w]
        cnt = dp[h][w]

        right = w + move
        down = h + move

        if right < N : 
            dp[h][right] += cnt
        

        if down < N :
            dp[down][w] += cnt

print(dp[-1][-1])
