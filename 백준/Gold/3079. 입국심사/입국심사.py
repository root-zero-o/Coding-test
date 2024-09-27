import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = []
for i in range(N):
    lst.append(int(input()))

# 기준 : 입국심사에 걸리는 총 시간
start = min(lst)
end = max(lst) * M
answer = 0
 
while start <= end :
    total = 0
    mid = (start + end) // 2

    for i in range(N):
        total += mid // lst[i]
    
    if total >= M :
        end = mid - 1
        answer = mid
    else :
        start = mid + 1
    
print(answer)
