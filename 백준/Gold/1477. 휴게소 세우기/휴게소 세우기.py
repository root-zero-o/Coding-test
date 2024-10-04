import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
lst = [0] + list(map(int, input().split())) + [L]
lst.sort()
distance = []
for i in range(len(lst) - 1):
    distance.append(lst[i+1] - lst[i])

start = 1
end = L - 1
res = 0

while start <= end :
    mid = start + (end - start) // 2
    cnt = 0
    for d in distance:
        if d > mid :
            cnt += (d - 1) // mid

    if cnt <= M :
        res = mid
        end = mid - 1
    else :
        start = mid + 1

print(res)