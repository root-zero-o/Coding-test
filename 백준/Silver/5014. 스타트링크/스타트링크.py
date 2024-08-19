from collections import deque
import sys 
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

visited = [0 for _ in range(F+1)]

def bfs():
    queue = deque([[S, 0]])
    visited[S] = 0

    while queue:
        v, dis = queue.popleft()
    
        if v == G : 
            return dis
        
        else :
            for nxt in [v + U, v - D]:
                if (0 < nxt <= F) and (visited[nxt] == 0 or visited[nxt] > dis+1) :
                    visited[nxt] = dis + 1
                    queue.append([nxt, dis+1])

    return 'use the stairs'

print(bfs())