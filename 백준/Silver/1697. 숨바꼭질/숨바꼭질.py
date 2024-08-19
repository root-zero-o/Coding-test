import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
max = 100000

# 방문 노드 저장
visited = [0] * (max+1)

# bfs
queue = deque([[N, 0]])

visited[N] = 1
while queue :
    v, dis = queue.popleft()
    if v == K : 
        print(dis)
        break
    else : 
        for i in [v+1, v-1, v*2]:
            if 0 <= i <= max and (not visited[i] or visited[i] > dis + 1):
                queue.append([i, dis+1])
                visited[i] = dis+1