import sys
from bisect import bisect_left, bisect_right 
input = sys.stdin.readline

# 입력 받기
T = int(input())
N = int(input())
lst_N = list(map(int, input().split()))
M = int(input())
lst_M = list(map(int, input().split()))

# 누적합
sum_N = []
sum_M = []
for i in range(N):
    for j in range(i+1, N+1):
        sum_N.append(sum(lst_N[i:j]))
for i in range(M):
    for j in range(i+1, M+1):
        sum_M.append(sum(lst_M[i:j]))

sum_N.sort()
sum_M.sort()

# 누적합 배열에 값이 몇 개 존재하는지
count = 0
for i in sum_N:
    target = T - i
    left = bisect_left(sum_M, target)
    right = bisect_right(sum_M, target)
    count += (right - left)

print(count)