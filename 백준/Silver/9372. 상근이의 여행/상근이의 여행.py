T = int(input())
for _ in range(T):
    N, M = list(map(int, input().split()))

    # 1) 인접 리스트 만들기
    lst = [[] for _ in range(N+1)]
    for i in range(M):
        start, end = map(int, input().split())
        lst[start].append(end)
        lst[end].append(start)
    
    # 2) 방문했던 노드 저장
    visited = [0] * (N+1)

    # 3) dfs
    def dfs(v):
        visited[v] = 1
        for j in lst[v]:
            if visited[j] == 0 :
                dfs(j)
    
    dfs(1)
    print(sum(visited) - 1)