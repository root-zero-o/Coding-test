import sys
input = sys.stdin.readline

MAX = 1000000
N, K = map(int, input().split())

pos_lst = [0] + [0 for _ in range(MAX)]
last_idx = 0

for _ in range(N):
    ice, pos = map(int, input().split())
    pos_lst[pos] = ice

    last_idx = max(last_idx, pos)

size = 2 * K + 1

window = sum(pos_lst[:size])

answer = window

for i in range(size, last_idx + 1):
    window = window + pos_lst[i] - pos_lst[i - size]
    answer = max(answer, window)

print(answer)