S = input()
T = input()

while(len(T) > 0) :
    last = T[-1]
    
    # 1) 마지막 글자가 A이면 => A만 잘라준다
    if last == 'A' :
        T = T[:-1]

    # 2) 마지막 글자가 B이면 => B를 자르고 뒤집음
    else :
        T = T[:-1]
        T = ''.join(list(reversed(list(T))))

    if T == S : break

if len(T) == 0 :
    print(0)
else : print(1)