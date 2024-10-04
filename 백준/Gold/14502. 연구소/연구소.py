# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0

import sys
import copy
from collections import deque
input = sys.stdin.readline

# 일단 입력 받기
H, W = map(int, input().split())
lab = []
for _ in range(H):
    temp = list(map(int, input().split()))
    lab.append(temp)
moves = [[1, 0], [0, -1], [-1, 0], [0, 1]]
answer = 0

# bfs(2차원) - 바이러스를 퍼뜨려서 안전구역 크기를 구한다
def bfs():
    global answer
    queue = deque()
    tmp_lab = copy.deepcopy(lab)

    # 바이러스에서부터 시작 -> 바이러스를 큐에 넣는다
    for h in range(H):
        for w in range(W):
            if tmp_lab[h][w] == 2 :
                queue.append((h, w))

    while queue:
        h, w = queue.popleft()
        
        for m in moves:
            nh = h + m[1]
            nw = w + m[0]
            
            if nw < 0 or nw >= W or nh < 0 or nh >= H: continue

            if tmp_lab[nh][nw] == 0 :
                tmp_lab[nh][nw] = 2
                queue.append((nh, nw))

    # 바이러스가 퍼진 후 안전구역이 몇 개인지 카운트해서 리턴
    safe = 0

    for i in range(H):
        safe += tmp_lab[i].count(0)
    
    answer = max(answer, safe)

def add_wall(cnt):
    if cnt == 3:
        bfs()
        return
    
    for h in range(H):
        for w in range(W):
            if lab[h][w] == 0 :
                lab[h][w] = 1
                add_wall(cnt+1)
                lab[h][w] = 0

add_wall(0)
print(answer)