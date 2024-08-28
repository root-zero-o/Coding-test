import sys
input = sys.stdin.readline

n, k = map(int, input().split())

triangle = [[1], [1, 1]]

for i in range(2, n):
    temp = []
    for j in range(i+1):
        if j == 0 : temp.append(1)
        elif j == i : temp.append(1)
        else :
            cur = triangle[i-1][j-1] + triangle[i-1][j]
            temp.append(cur)
    triangle.append(temp)

print(triangle[n-1][k-1])