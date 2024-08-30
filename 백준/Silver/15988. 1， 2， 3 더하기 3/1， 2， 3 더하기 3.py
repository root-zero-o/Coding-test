import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    if N == 1 :
        print(1)
    elif N == 2 : print(2)
    elif N == 3 : print(4)
    else :
        a, b, c = 1, 2, 4

        for i in range(3, N):
            a, b, c  = b, c, (a+b+c) % 1000000009

        print(c)
