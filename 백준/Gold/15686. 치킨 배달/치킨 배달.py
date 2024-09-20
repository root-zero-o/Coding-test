import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 치킨집, 집 좌표들 구하기
chicken = []
home = []

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1 :
            home.append([j, i])
        elif row[j] == 2 :
            chicken.append([j, i])

selected = []
answer = 999999

def solve(idx):
    global answer

    if len(selected) == M :
        temp = 0
        for i in home:
            dis = 999
            for j in selected:
                dis = min(dis, abs(chicken[j][0] - i[0]) + abs(chicken[j][1] - i[1]))
            temp += dis
        answer = min(answer, temp)
        return
    
    for i in range(len(chicken)):
        if i <= idx :
            continue

        selected.append(i)
        solve(i)
        selected.pop()

solve(-1)
print(answer)