N = int(input())

dp = [[1 for _ in range(10)] for _ in range(N+1)]

if N > 1 :
    for i in range(2, N+1) :
        for j in range(10):
            if j == 0 :
                dp[i][j] = 1
            else :
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(sum(dp[-1]) % 10007)

