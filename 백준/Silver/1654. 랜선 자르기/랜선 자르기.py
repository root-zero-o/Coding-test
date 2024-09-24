import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lines = []
for i in range(K):
    lines.append(int(input()))
lines.sort()

start = 0
end = lines[-1]
answer = 0

while(start <= end):
    mid = (start + end) // 2

    if mid == 0 :
        mid = 1
    
    temp = 0
    for i in range(K):
        temp += lines[i] // mid

    if temp >= N :
        answer = mid
        start = mid + 1
    else :
        end = mid - 1

print(answer)

