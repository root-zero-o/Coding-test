N = int(input())
K = int(input())
lst = list(map(int, input().split()))

# 1) 오름차순 정렬
lst.sort()

# 2) K가 N보다 크면 0 출력
if(K >= N):
    print(0)

else :
    # 3) 센서 사이의 간격 리스트 만들기(오름차순)
    gap = []
    for i in range(1, N):
        gap.append(lst[i] - lst[i - 1])
    gap.sort()

    # 4) 기지국 수 -1 만큼 제외(그 부분에서 나눔) 
    for i in range(K - 1):
        gap.pop()

    # 5) 합 구해 출력
    print(sum(gap))