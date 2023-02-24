
# 구간합
T = int(input())
for a in range(T):
    N, M = map(int, input().split())
    n_list = list(map(int, input().split()))
    ans_list = []
    maxV = 0
    minV = 0

    for i in range(0, N- M +1): #구간이 생기는 수 만큼
        ans = 0
        for j in range(M): #구간의 길이만큼
            ans += n_list[i+j] #구간의 합 구하기
        ans_list.append(ans) #구한 구간의 합을 리스트에 넣어주기

    for x in range(len(ans_list)): #max구하기
        if x == 0: #첫번째 인덱스는 바로 max값
            maxV = ans_list[0]
        elif ans_list[x] > maxV: # 그 다음 값이 크면 바로 교체
            maxV = ans_list[x]
    for y in range(len(ans_list)): #min구하기
        if y == 0:
            minV = ans_list[0]
        elif ans_list[y] < minV:
            minV = ans_list[y]
    print(f'#{a+1} {maxV - minV}')