import sys
input = sys.stdin.readline

# 1) 입력 받기
N, M = map(int, input().split())
trees = sorted(list(map(int, input().split())))

# 2) 이진탐색
start = 0
end = trees[-1]
answer = 0

while(start < end):
    mid = (start + end) // 2

    temp = 0
    for i in range(N):
        if trees[i] > mid :
            temp += trees[i] - mid
        
    if temp >= M :
        answer = mid
        start = mid+1
    else :
        end = mid

print(answer)