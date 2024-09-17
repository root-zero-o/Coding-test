import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))    

visited = [0] * 4
answer_max = -1000000000
answer_min = 1000000000

def calc(left, right, idx):
    if idx == 0 :
        return left + right
    elif idx == 1 :
        return left - right
    elif idx == 2 :
        return left * right
    else :
        if left >= 0 :
            return left // right
        else :
            return ((left * -1) // right) * -1

def backTracking(now, idx):
    global answer_max, answer_min
    if idx == N-1 :
        answer_max = max(answer_max, now)
        answer_min = min(answer_min, now)
        return
    
    for j in range(4) :
         # 연산자가 0개 일 때
        if op[j] == 0:
            continue
        # 이미 연산자를 다 사용했을 때
        if visited[j] == op[j]:
            continue
            
        visited[j] += 1
        temp = calc(now, nums[idx+1], j)
        backTracking(temp, idx+1)
        visited[j] -= 1

backTracking(nums[0], 0)
print(int(answer_max))
print(int(answer_min))