import sys
input = sys.stdin.readline

N, H = map(int, input().split())
bot = [] # 석순
top = [] # 종유석

for i in range(N):
    if i % 2 == 0 :
        bot.append(int(input()))
    else :
        top.append(int(input()))

bot.sort()
top.sort()

def left_bound(lst, target):
    start = 0
    end = len(lst)
    while start < end :
        mid = (start + end) // 2
        if lst[mid] >= target:
            end = mid
        else :
            start = mid +1
    return start

crash = []

for i in range(1, H+1):
    crash_bot = len(bot) - left_bound(bot, i)
    crash_top = len(top) - left_bound(top, H - i + 1)
    temp = crash_bot + crash_top

    crash.append(temp)

print(min(crash), crash.count(min(crash)))