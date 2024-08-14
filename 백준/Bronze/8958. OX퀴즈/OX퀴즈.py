N = int(input())

for _ in range(1, N+1):
    str = input()

    cnt = 0
    cur = 0
    for i in range(len(str)):
        if(str[i] == 'O'):
            cur += 1
            cnt += cur
        else : 
            cur = 0
    
    print(cnt)