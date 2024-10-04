import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [0] * (N+1)

def bfs(start):
    queue = deque([start])
    visited[start] = 1

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[v] + 1
    
bfs(1)
answer = 0
for i in visited :
    if 1 < i < 4:
        answer += 1
    
print(answer)