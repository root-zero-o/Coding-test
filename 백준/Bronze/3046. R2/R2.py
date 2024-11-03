import sys
input = sys.stdin.readline

N, S = map(int, input().split())

print(S * 2 - N)