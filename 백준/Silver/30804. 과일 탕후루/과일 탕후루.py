import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

left = 0
right = 0
answer = 0
fruit_count = defaultdict(int)

while right < N :
    fruit_count[lst[right]] += 1

    while len(fruit_count) > 2 :
        fruit_count[lst[left]] -= 1
        if fruit_count[lst[left]] == 0 :
            del fruit_count[lst[left]]
        left += 1

    answer = max(answer, right - left + 1)
    right += 1  

print(answer)