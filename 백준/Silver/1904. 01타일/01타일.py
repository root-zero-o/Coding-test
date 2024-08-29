N = int(input())

# 피보나치 수열 형태로 경우의 수가 늘어남
# 짝수 자리수 -> 바로 직전 짝수 자리수 경우에 00을 붙임
# 홀수 자리수 -> 바로 직전 홀수 자리수 경우에 1을 붙임

prev = 1
next = 2

if N == 1 :
    print(1)
else :
    for i in range(2, N):
        prev, next = next % 15746, (prev+next) % 15746

    print(next)

