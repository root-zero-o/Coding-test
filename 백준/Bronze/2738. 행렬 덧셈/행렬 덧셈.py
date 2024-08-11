N, M = map(int, input().split())
lstA = [list(map(int, input().split())) for i in range(N)]
lstB = []
for i in range(N):
    lstB.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        lstA[i][j] += lstB[i][j]

for i in range(N):
    print(*lstA[i])