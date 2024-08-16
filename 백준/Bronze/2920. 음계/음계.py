lst = list(map(int, input().split()))

mixed = False

for i in range(1, 8):
    gap = lst[i] - lst[i-1]
    if abs(gap) != 1 :
        mixed = True
        break
    
if(mixed): print('mixed')
elif lst[1] - lst[0] > 0 : print('ascending')
else : print('descending')