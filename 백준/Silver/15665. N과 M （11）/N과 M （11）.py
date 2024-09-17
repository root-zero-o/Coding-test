# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))

answer = []

def backTracking():
    if len(answer) == M :
        print(*answer)
        return
    
    temp = 0
    
    for i in lst:
        if i != temp:
            answer.append(i)
            temp = i
            backTracking()
            answer.pop()

backTracking()