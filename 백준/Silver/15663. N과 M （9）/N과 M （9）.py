# N개의 자연수 중에서 M개를 고른 수열
N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

answer = []
visited = [0] * N

def backTracking(x):
    if len(answer) == M :
        print(" ".join(map(str, answer)))
        return

    temp = 0

    for i in range(N):
        if not visited[i] and temp != lst[i] :
            answer.append(lst[i])
            visited[i] = 1
            temp = lst[i]
            backTracking(i)
            answer.pop()
            visited[i] = 0

backTracking(-1)