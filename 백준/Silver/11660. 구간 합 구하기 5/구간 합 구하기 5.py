import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [[0 for _ in range(N+1)]]
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(N):
    temp = [0] + list(map(int, input().split()))
    nums.append(temp)

for h in range(1, N+1):
    for w in range(1, N+1):
        dp[h][w] = nums[h][w] + dp[h-1][w] + dp[h][w-1] - dp[h-1][w-1]

for _ in range(M):
    h1, w1, h2, w2 = map(int, input().split())

    answer = dp[h2][w2] - dp[h1-1][w2] - dp[h2][w1-1] + dp[h1-1][w1-1]
    print(answer)