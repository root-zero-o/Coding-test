import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * 91
# 자리가 늘어날 수록 경우의 수가 피보나치 수열로 늘어난다

dp[1] = 1
dp[2] = 1

for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])