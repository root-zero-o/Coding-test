T = int(input())

for _ in range(T):
    N = int(input())
    
    if N == 1 : print(1)
    elif N == 2 : print(2)
    elif N == 3 : print(4)
    else :
        memo = [0] * (N+1)
        # 기본 값 넣어두기
        memo[1] = 1
        memo[2] = 2
        memo[3] = 4
        
        for i in range(N+1):
            if i > 3 :
                memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
        
        print(memo[N])