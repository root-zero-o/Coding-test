import sys
input = sys.stdin.readline

N = int(input())
lst_N = sorted(list(map(int, input().split())))
M = int(input())
lst_M = list(map(int, input().split()))

answer = []

def binary_search(start, end, target):
    s = start
    e = end
    cnt = 0

    while(s <= e):
        mid = (s + e) // 2
        if lst_N[mid] < lst_M[target] :
            s = mid + 1
        elif lst_N[mid] == lst_M[target] :
            cnt += 1
            break
        else:
            e = mid - 1
    return cnt

for i in range(M):
    num = binary_search(0, N-1, i)
    answer.append(num)

print(*answer)