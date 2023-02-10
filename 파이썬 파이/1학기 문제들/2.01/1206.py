import sys

sys.stdin = open("input.txt")

#view
def my_max(x_list):
    maxV = 0
    for x in range(len(x_list)): #max구하기
        if x == 0: #첫번째 인덱스는 바로 max값
            maxV = x_list[0]
        elif x_list[x] > maxV: # 그 다음 값이 크면 바로 교체
            maxV = x_list[x]
    return maxV


for a in range(10):
    N = int(input())
    n_list = list(map(int, input().split()))

    cnt = 0 #cnt는 누적
    for i in range(2, N-2):
        ans_list = [] #list는 계속 초기화
        ans_list.append(n_list[i - 2])
        ans_list.append(n_list[i - 1])
        ans_list.append(n_list[i + 1])
        ans_list.append(n_list[i + 2])

        if my_max(ans_list) < n_list[i]:
            cnt += (n_list[i] - my_max(ans_list))
    print(f'#{a+1} {cnt}')



#양 옆에 4개 리스트에 어펜드
#if 하나라도 i번째보다 크면 ㄴㄴ
#if 전부 작으면 그 중 가장 큰 값 i번째 - 가장 큰값 만큼 카운트