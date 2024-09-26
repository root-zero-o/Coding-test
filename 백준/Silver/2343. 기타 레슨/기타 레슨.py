import sys
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
lst = list(map(int, input().split()))

start = max(lst)
end = sum(lst)
answer = 0

while start <= end :
    mid = (start + end) // 2
    
    total = 0
    count = 1
    for i in lst :
        if total + i > mid :
            count += 1
            total = 0
        total += i
    
    if count <= M:
        answer = mid
        end = mid - 1
    else :
        start = mid + 1

print(answer)