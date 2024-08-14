N = input()

for i in range(ord('a'), ord('z') + 1):
    try:
        print(N.index(chr(i)))
    except: print(-1)