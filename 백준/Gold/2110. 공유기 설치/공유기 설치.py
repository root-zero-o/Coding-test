import sys
input = sys.stdin.readline

# 입력 받기
N, C = map(int, input().split())
lst = []
for i in range(N):
    lst.append(int(input()))
lst.sort()

start = 1
end = lst[-1] - lst[0]
answer = 0

while start <= end : 
    mid = (start + end) // 2
    count = 1
    cur = lst[0]

    for i in lst :
        if i >= cur + mid :
            count += 1
            cur = i
    
    if count >= C :
        start = mid + 1
        answer = mid
    else :
        end = mid - 1

print(answer)