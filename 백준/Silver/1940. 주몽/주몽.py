N = int(input())
M = int(input())
lst = list(map(int, input().split()))

lst.sort()

left = 0
right = N - 1
cnt = 0
while left < right :
    temp = lst[left] + lst[right]
    if temp < M :
        left += 1
    elif temp > M :
        right -= 1
    else : 
        cnt +=1
        left +=1

print(cnt)