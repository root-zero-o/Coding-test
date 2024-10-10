# 스택 사용해서 다시 풀기

def solution(s):
    st = []
    
    for i in s :
        if i == '(':
            st.append(i)
        else :
            try:
                st.pop()
            except IndexError:
                return False
    
    return len(st) == 0
    