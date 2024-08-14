N = 1
for i in range(3) :
    N *= int(input())

lst = list(str(N))

for i in range(0, 10):
    print(lst.count(str(i)))