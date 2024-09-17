import sys
input = sys.stdin.readline

N = int(input())
lst = list(input().split())

visited = [0] * 10
answer_max = ""
answer_min = ""

def check(i, j, k):
    if k == "<":
        return i < j
    else :
        return i > j

def solve(idx, s):
    global answer_max, answer_min

    if idx == N+1:
        if len(answer_min) == 0 :
            answer_min = s
        else :
            answer_max = s
        return
    
    for i in range(10):
        if not visited[i]:
            if idx == 0 or check(s[-1], str(i), lst[idx - 1]):
                visited[i] = 1
                solve(idx+1, s+str(i))
                visited[i] = 0

solve(0, "")
print(answer_max)
print(answer_min)

# 어렵당