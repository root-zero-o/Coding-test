# 10
# 6 3 2 10 10 10 -10 -10 7 3
# 8
# 10 9 -5 2 3 4 5 -10
import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

# 1) 입력 받기
N = int(input())
lst_N = sorted(list(map(int, input().split())))
M = int(input())
lst_M = list(map(int, input().split()))

answer = []

# 2) binary search
def count_by_range(left_value, right_value):
    right_index = bisect_right(lst_N, right_value)
    left_index = bisect_left(lst_N, left_value)
    return right_index - left_index

# 3) 반복
for i in range(M):
    num = count_by_range(lst_M[i], lst_M[i])
    answer.append(num)

print(*answer)