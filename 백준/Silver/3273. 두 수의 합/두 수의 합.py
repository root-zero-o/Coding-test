N = int(input())
lst = list(map(int, input().split()))
X = int(input())

lst.sort()
left = 0
right = N - 1
count = 0

while left < right :
    sum = lst[left] + lst[right]

    if sum < X :
        left += 1
    elif sum > X :
        right -= 1
    else :
        count += 1
        left += 1

print(count)