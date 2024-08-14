lst = list(map(int, input().split()))

if lst[0] > lst[1]: print('>')
elif lst[0] < lst[1] : print('<')
else : print('==')