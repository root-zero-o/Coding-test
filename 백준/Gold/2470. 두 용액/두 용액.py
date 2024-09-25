N = int(input())
lst = sorted(list(map(int, input().split())))

start = 0
end = N - 1

answer_cnt = abs(lst[start] + lst[end])
answer_s = lst[start]
answer_e = lst[end]

while(start < end):
    temp = lst[start] + lst[end]

    if abs(temp) <= abs(answer_cnt):
        answer_cnt = temp
        answer_s = lst[start]
        answer_e = lst[end]
    
    if temp == 0 :
        break
    elif temp < 0 :
        start += 1
    else : 
        end -= 1

print(answer_s, answer_e)