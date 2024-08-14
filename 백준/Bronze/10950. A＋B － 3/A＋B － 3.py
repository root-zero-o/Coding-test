N = int(input())
lst = [list(map(int, input().split())) for i in range(N)]

for i in range(N):
    first, second = lst[i]
    print(first + second)