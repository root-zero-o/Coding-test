import sys
input = sys.stdin.readline

hamburgers = []
drinks = []
for _ in range(3):
    hamburgers.append(int(input()))
for _ in range(2):
    drinks.append(int(input()))

print(min(hamburgers) + min(drinks) - 50)