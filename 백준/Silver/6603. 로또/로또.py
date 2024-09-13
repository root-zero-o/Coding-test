import sys
input = sys.stdin.readline

while True:
    lst = list(map(int, input().split()))

    k = lst[0]
    S = lst[1:]

    if k == 0 :
        break

    answer = []
    def backTracking(x):
        if len(answer) == 6 :
            print(" ".join(map(str, answer)))
            return
        
        for i in S :
            if i not in answer and i > x:
                answer.append(i)
                backTracking(i)
                answer.pop()
    
    backTracking(0)
    print()