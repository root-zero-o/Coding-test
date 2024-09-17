# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))

answer = []
def backTracking(x):
    if len(answer) == M :
        print(*answer)
        return
    
    temp = 0

    for i in lst :
        if i != temp and i >= x :
            answer.append(i)
            temp = i
            backTracking(i)
            answer.pop()

backTracking(-1)