import sys
input = sys.stdin.readline

N, S = map(int, input().split())
lst = list(map(int, input().split()))
answer = []
cnt = 0

def backTracking(x):
    global cnt
    if len(answer) > 0 and sum(answer) == S :
        cnt += 1
    for i in range(x, N) :
        answer.append(lst[i])
        backTracking(i+1)
        answer.pop()
             
backTracking(0)
print(cnt)