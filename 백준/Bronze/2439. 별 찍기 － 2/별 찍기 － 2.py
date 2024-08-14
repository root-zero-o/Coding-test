N = int(input())

for i in range(N):
    temp = []
    for j in range(N):
        if i >= N - j - 1 : temp.append('*')
        else : temp.append(' ')
    print(''.join(temp))