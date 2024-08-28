N = int(input())

memo = [0] * (1001)
memo[1] = 1 # SK
memo[2] = 0 # CY
memo[3] = 1 # SK

# n-1, n-3의 반대를 저장
for i in range(4, N+1):
    if memo[i-1] == 1 or memo[i-3] == 1 :
        memo[i] = 0
    else :
        memo[i] = 1

if memo[N] == 1 : print('SK')
else : print('CY')