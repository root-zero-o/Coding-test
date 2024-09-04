N = int(input())

lst = [[0, 0]]
for _ in range(N):
    lst.append(list(map(int, input().split())))

if N == 1 :
    day, value = lst[1]
    if N < day : print(0)
    else : print(value)

else :
    dp = [0] * (N+1)

    for i in range(1, N+1):
        day, value = lst[N+1 - i] # 거꾸로


        if day == 1 :
            dp[i] = dp[i-1] + value
        
        else :
            if(i < day): 
                dp[i] = dp[i-1]
            else :
                dp[i] = max(dp[i-1], dp[i - day] + value) 

    print(dp[-1])