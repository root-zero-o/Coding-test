import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

answer = []
visited = [0] * N
maxCnt = 0

def backTracking(x):
    global maxCnt
    if len(answer) == N:
        value = 0
        for i in range(N-1):
            value += abs(answer[i] - answer[i+1])
        maxCnt = max(maxCnt, value)
        return
    
    for i in range(N) :
        if not visited[i] :
            answer.append(lst[i])
            visited[i] = 1
            backTracking(i)
            answer.pop()
            visited[i] = 0

backTracking(-1)
print(maxCnt)