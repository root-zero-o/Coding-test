from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

# 인접 리스트
lst = [[] for _ in range(N+1)]
for i in range(N-1):
    start, end = map(int, input().split())
    lst[start].append(end)
    lst[end].append(start)

# 방문 노드 저장
visited = [0] * (N+1)

# bfs
parents = []
queue = deque([1])
while queue :
    v = queue.popleft()
    for i in lst[v]:
        if not visited[i] :
            visited[i] = v
            queue.append(i)

print(*visited[2:], sep="\n")