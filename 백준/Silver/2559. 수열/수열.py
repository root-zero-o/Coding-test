# 10 2
# 3 -2 -4 -9 0 3 7 13 8 -3

N, K = map(int, input().split())
lst = list(map(int, input().split()))

left = 0
right = K
answer = 0
prev = 0

for i in range(left, K):
    prev += lst[i]
answer = prev

while right < N :
    temp = prev - lst[left] + lst[right]
    
    answer = max(answer, temp)
    prev = temp
    left += 1
    right += 1

print(answer)