def solution(s):
    lst = list(s)
    left = []
    right  = []
    for i in range(len(lst)):
        if lst[i] == '(':
            left.append(i)
        else :
            right.append(i)
    if len(left) != len(right):
        return False
    
    for i in range(len(left)):
        if left[i] > right[i]:
            return False
            break
    return True
