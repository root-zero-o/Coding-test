import sys
input = sys.stdin.readline

N = int(input()) # 지방의 수
lst = list(map(int, input().split()))
M = int(input()) # 총 예산

def binarySearch(start, end):
    mid = (start + end) // 2

    if start == mid or end == mid :
        return mid

    temp = 0
    for i in lst:
        if i > mid :
            temp += mid
        else :
            temp += i
    
    if temp > M :
        return binarySearch(start, mid)
    else :
        return binarySearch(mid, end)

if sum(lst) > M :
    answer = binarySearch(0, max(lst))  
    print(answer)
else :
    print(max(lst))