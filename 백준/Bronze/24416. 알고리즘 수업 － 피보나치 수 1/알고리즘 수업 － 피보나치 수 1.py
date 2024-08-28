N = int(input())

cnt = 0
f = [0] * 41
f[1] = 1
f[2] = 1


def fib2(n):
    global cnt, f
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
        cnt += 1

fib2(N)
print(f[N], cnt, end=" ")