import sys
input = sys.stdin.readline
N = int(input())

f = [0] * (1001)
f[1] = 1 # CY
f[2] = 0 # SK
f[3] = 1 # CY

for i in range(4, N+1):
    if f[i-1] == 1 or f[i-3] == 1:
        f[i] = 0
    else :
        f[i] = 1

if f[N] == 1 : print("CY")
else : print("SK")