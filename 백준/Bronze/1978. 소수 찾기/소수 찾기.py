import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

cnt = 0
for i in range(N):
    num = lst[i]
    if num > 1 :
        for j in range(2, num):
            if num % j == 0:
                cnt += 1
                break
    else : cnt += 1

print(N - cnt)