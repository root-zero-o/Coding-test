import math

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    room = 0
    floor = 0

    if N % H == 0 : floor = H
    else : floor = N % H

    room += math.ceil(N / H)
    
    answer = str(floor)
    if room < 10 : 
        answer += '0' + str(room)
    else : 
        answer += str(room)

    print(answer)