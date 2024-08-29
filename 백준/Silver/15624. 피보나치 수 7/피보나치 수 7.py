import sys
input = sys.stdin.readline

N = int(input())

a = 0
b = 1

if N == 0 :
    print(a)
else:
    for i in range(2, N+1):
        a, b = b % 1000000007, (a+b) % 1000000007
 
    print(b)
