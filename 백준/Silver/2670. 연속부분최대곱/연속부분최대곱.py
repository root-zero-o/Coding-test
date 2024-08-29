N = int(input())
lst = []
for _ in range(N):
    lst.append(float(input()))

for i in range(1, N):
    lst[i] = max(lst[i], lst[i-1] * lst[i])

print('%0.3f' % max(lst))
