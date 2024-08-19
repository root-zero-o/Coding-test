import sys
input = sys.stdin.readline
from collections import deque

N, M, R = map(int, input().split())

# 1) 인접 리스트 
lst = [[] for _ in range(N+1)]
for i in range(M):
    start, end = map(int, input().split())
    lst[start].append(end)
    lst[end].append(start)

for i in range(N+1):
    lst[i].sort(reverse=True)

# 2) 방문 노드 저장
visited = [0] * (N+1)

# 3) bfs
queue = deque([R])
cnt = 1
visited[R] = cnt
while queue : 
    v = queue.popleft()
    for j in lst[v]:
        if visited[j] == 0 : 
            cnt += 1
            visited[j] = cnt
            queue.append(j)

print(*visited[1:],sep='\n')