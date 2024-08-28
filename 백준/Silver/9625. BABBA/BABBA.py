import sys
input = sys.stdin.readline

K = int(input())

dp = [ [1, 0], [0, 1]]


for i in range(2, K+1) :
    prevA, prevB = dp[i-1]

    A = prevB 
    B = prevA + prevB

    dp.append([A, B])

print(*dp[-1])
