import sys
input = sys.stdin.readline

L, C = map(int, input().split())
lst = sorted(list(input().split()))

v = ['a', 'e', 'i', 'o', 'u']

answer = []

def solve(x, cnt1, cnt2):

    if len(answer) == L and cnt1 > 0 and cnt2 > 1 :
        print("".join(map(str, answer)))
        return
    
    for i in range(C) :
        if i <= x : 
            continue

        answer.append(lst[i])
        if lst[i] not in v :
            solve(i, cnt1, cnt2+1)
        else :
            solve(i, cnt1+1, cnt2)
        answer.pop()

solve(-1, 0, 0)