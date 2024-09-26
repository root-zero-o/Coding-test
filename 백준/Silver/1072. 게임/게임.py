import sys
input = sys.stdin.readline

X, Y = map(int, input().split()) # X : 게임 횟수, Y : 이긴 게임
Z = 100 * Y // X

start = X
end = 1000000000 + X
lose = X - Y # 진 게임 수
answer = 0

while start <= end:
    mid = (start + end) // 2
    temp_z = 100 * (mid - lose) // mid

    if temp_z == Z :
        start = mid + 1
    else : 
        end = mid - 1
        answer = mid

if not answer :
    print(-1)
else :
    print(answer - X)