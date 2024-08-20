import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
max = 100000

visited = [0] * (max+1)
move = [2, -1, 1]

# bfs
queue = deque([[N, 0]])

while queue :
    pos, time = queue.popleft()

    if pos == K :
        print(time)
        break

    for i in range(3):
        if i == 0 :
            next = pos * move[i]

            if 0 <= next <= max and visited[next] == 0 :
                queue.append([next, time])
                visited[next] = 1
            
        else :
            next = pos + move[i]

            if 0 <= next <= max and visited[next] == 0 :
                queue.append([next, time+1])
                visited[next] = 1