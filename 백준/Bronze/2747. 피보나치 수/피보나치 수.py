N = int(input())

memo = [0] * 46

def fibonacci(x):
    if x == 1 or x == 2:
        return 1
    
    if memo[x] != 0 :
        return memo[x]
    
    memo[x] = fibonacci(x-1) + fibonacci(x-2)
    return memo[x]

print(fibonacci(N))