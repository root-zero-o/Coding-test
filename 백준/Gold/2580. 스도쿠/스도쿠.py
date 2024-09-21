import sys
input = sys.stdin.readline

graph = []
for i in range(9):
    graph.append(list(map(int, input().split())))

blank = [] # 빈 칸 좌표
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0 :
            blank.append([i, j])

def checkRow(x, num):
    for i in range(9):
        if graph[x][i] == num:
            return False
    return True

def checkCol(y, num):
    for i in range(9):
        if graph[i][y] == num:
            return False
    return True

def checkRec(x, y, num):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if graph[nx+i][ny+j] == num:
                return False
    return True

def solve(idx):
    if idx == len(blank):
        for i in range(9):
            print(*graph[i])
        exit(0)
    
    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]

        if checkRow(x, i) and checkCol(y, i) and checkRec(x, y, i):
            graph[x][y] = i
            solve(idx+1)
            graph[x][y] = 0

solve(0)