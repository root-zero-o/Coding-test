T = int(input())

for _ in range(T):
    len = int(input())
    
    # 1) 이차원 배열 만들기
    lst = [[] for i in range(len)]
    temp = list(map(int, input().split()))
    for i in range(len):
        lst[i].append(i+1)
        lst[i].append(temp[i])

    # 2) 인접 리스트 만들기
    graph = [[] for i in range(len + 1)]
    for i in range(len):
        start, end = lst[i]
        graph[start].append(end)
        graph[end].append(start)        
    
    # 3) 방문 노드 저장
    visited = [0] * (len + 1)

    # 4) dfs 정의
    def dfs(start):
        visited[start] = 1
        for j in graph[start]:
            if not visited[j] :
                visited[j] = 1
                dfs(j)

    # 5) 카운트
    cnt = 0
    for i in range(1, len+1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    
    print(cnt)