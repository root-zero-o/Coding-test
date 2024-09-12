import sys
input = sys.stdin.readline

N = int(input())
answer = []

def backTracking():
    if(len(answer) == N):
        print(" ".join(map(str, answer)))
        return
    
    for i in range(1, N+1):
        if i not in answer:
            answer.append(i)
            backTracking()
            answer.pop()

backTracking()