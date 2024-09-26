import sys
input = sys.stdin.readline

N = int(input())
lst = sorted(list(map(int, input().split())))
good_nums = set()

count = 0
for i in range(N):
    if lst[i] in good_nums:
        count += 1
        continue

    start = 0
    end = N - 1

    while start < end :
        temp = lst[start] + lst[end]

        if start == i :
            start += 1
            continue
        
        if end == i :
            end -= 1
            continue

        if temp == lst[i]:
            count += 1
            good_nums.add(lst[i])
            break
        elif temp < lst[i]:
            start += 1
        elif temp > lst[i]:
            end -= 1

print(count)

