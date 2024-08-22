import sys
input = sys.stdin.readline
from collections import deque

A, B, C = map(int, input().split())

max = 200
lst = []

# 방문 노드 저장
visited = [[0 for _ in range(max+1)] for _ in range(max+1)]

# bfs
queue = deque([[0,0]])
visited[0][0] = 1

def pour(x, y):
    if not visited[x][y] :
        visited[x][y] = 1
        queue.append([x, y])

while queue:
    a, b = queue.popleft()

    c = C - a - b

    if a == 0 :
        lst.append(c)
    
    # a -> b
    water = min(a, B - b)
    pour(a - water, b + water)

    # a -> c
    water = min(a, C - c)
    pour(a - water, b)

    # b -> a
    water = min(b, A - a)
    pour(a + water, b - water)

    # b -> c
    water = min(b, C - c)
    pour(a, b - water)

    # c -> a
    water = min(c, A - a)
    pour(a + water, b)

    # c -> b
    water = min(c, B - b)
    pour(a, b + water)

lst.sort()
print(*lst)

# 어렵다..