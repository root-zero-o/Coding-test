import sys
input = sys.stdin.readline

N = int(input())
costs = []
for i in range(N):
    costs.append(list(map(int, input().split())))

answer = sys.maxsize # 가장 큰 정수
visited = [0] * N # 방문한 도시 리스트

def dfs(start, now, total):
    global answer

    # 가지치기
    if answer < total:
        return
    
    if start == now and 0 not in visited:
        if total < answer:
            answer = total
        return
    
    for i in range(N):
        if not costs[now][i] :
            continue
        
        if visited[i]:
            continue
        
        visited[i] = 1
        dfs(start, i, total + costs[now][i])
        visited[i] = 0

dfs(0, 0, 0)
print(answer)