N = int(input())

memo = [0] * 1001
memo[1] = 1
memo[2] = 2

for i in range(3, N+1):
    memo[i] = memo[i-1] + memo[i-2]

print(memo[N] % 10007)