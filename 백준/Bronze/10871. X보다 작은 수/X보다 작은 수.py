N, X = map(int, input().split())

lst = list(map(int, input().split()))

answer = []
for i in range(N):
    if lst[i] < X :
        answer.append(lst[i]) 

print(*answer)