import sys
input = sys.stdin.readline

N = int(input())
lst = sorted(map(int, input().split()))

answer_s = 0
answer_m = 0
answer_e = 0
min_abs = 3000000001

for start in range(N):
    mid = start + 1
    end = N - 1

    while mid < end :
        temp = lst[start] + lst[end] + lst[mid]

        if abs(temp) < min_abs:
            answer_s = lst[start]
            answer_m = lst[mid]
            answer_e = lst[end]
            min_abs = abs(temp)
        
        if temp == 0 :
            break
        if temp > 0 :
            end -= 1
        else :
            mid += 1

print(answer_s, answer_m, answer_e)