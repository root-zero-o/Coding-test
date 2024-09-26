import sys
input = sys.stdin.readline

N = int(input())
lst_N = sorted(list(map(int, input().split())))
M = int(input())
lst_M = list(map(int, input().split()))

def binary_search(target):
    start = 0
    end = N - 1
    temp = 0
    while start <= end :
        mid = (start + end) // 2

        if lst_N[mid] == lst_M[target]:
            temp = 1
            break

        if lst_N[mid] < lst_M[target]:
            start = mid + 1
        else :
            end = mid - 1
    return temp

for i in range(M):
    print(binary_search(i))