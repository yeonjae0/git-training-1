#Min Max의 차 구하기
T = int(input())
for i in range(T):
    #print(f'i는{i}번째 반복')
    N = int(input())
    n_list = list(map(int, input().split()))  # 수열을 리스트로 받기
    minV = 0
    maxV = 0
    for x in range(len(n_list)): #max구하기
        #print(f'x는{x}번째 반복')
        if x == 0: #첫번째 인덱스는 바로 max값
            maxV = n_list[0]
        elif n_list[x] > maxV: # 그 다음 값이 크면 바로 교체
            maxV = n_list[x]
        #print(f'maxV는 {maxV}')

    for y in range(len(n_list)): #min구하기
        #print(f'y는{y}번째 반복')
        if y == 0:
            minV = n_list[0]
        elif n_list[y] < minV:
            minV = n_list[y]
        #print(f'minV는 {minV}')
    print(f'#{i+1} {maxV - minV}')


