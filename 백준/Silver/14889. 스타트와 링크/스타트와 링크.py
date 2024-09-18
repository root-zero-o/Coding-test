import sys
input = sys.stdin.readline

N = int(input())
val = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
answer = 100

def solve(cnt, now):
    global answer
    if cnt == N // 2 :
        start = 0
        link = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += val[i][j]
                elif not visited[i] and not visited[j] :
                    link += val[i][j]
        answer = min(answer, abs(start - link))
        return

    for i in range(now, N):
        if visited[i] :
            continue
        
        visited[i] = 1
        solve(cnt+1, i+1)
        visited[i] = 0
          
solve(0, 0)
print(answer)