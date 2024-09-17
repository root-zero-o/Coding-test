# N개의 자연수 중에서 M개를 고른 수열
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))

visited = [0] * N
answer = []

def backTracking(x):
    if len(answer) == M :
        print(*answer)
        return

    temp = 0
    
    for i in range(N):
        if not visited[i] and lst[i] >= x and temp != lst[i] :
            answer.append(lst[i])
            temp = lst[i]
            visited[i] = 1
            backTracking(lst[i])
            answer.pop()
            visited[i] = 0

backTracking(-1)