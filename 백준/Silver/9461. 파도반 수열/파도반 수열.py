# idx 5 차이나는 수를 더해서 만들어진다

T = int(input())
for _ in range(T):
    N = int(input())

    # 일단 초기화,,
    nums = [0] * 101
    nums[1] = 1
    nums[2] = 1
    nums[3] = 1
    nums[4] = 2
    nums[5] = 2
    
    if N < 6 :
        print(nums[N])
    else :
        for i in range(6, N+1):
            nums[i] = nums[i-1] + nums[i-5]
        
        print(nums[N])
