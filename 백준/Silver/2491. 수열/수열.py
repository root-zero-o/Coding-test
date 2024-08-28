N = int(input())

lst = list(map(int, input().split()))

mins = [0] * (N+1)
mins[0] = 1

maxs = [0] * (N+1)
maxs[0] = 1

# 연속해서 작아지는 수
for i in range(1, N):
    if lst[i] <= lst[i-1]:
        mins[i] = mins[i-1] + 1
    
    else :
        mins[i] = 1

# 연속해서 커지는 수
for i in range(1, N):
    if lst[i] >= lst[i-1]:
        maxs[i] = maxs[i-1] + 1
    else :
        maxs[i] = 1

print(max(max(mins), max(maxs)))
 
    