import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')
#1 회전각도에 따른 위치값을 저장
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    a1 = [[0] * N for _ in range(N)] #90도
    a2 = [[0] * N for _ in range(N)]
    a3 = [[0] * N for _ in range(N)]
    # a1, a2, a3 = [[[0] * N for _ in range(N)] for _ in range(3)]

    #회전 각도에 따른 위치값을 저장
    for i in range(N):
        for j in range(N):
            a1[i][j] = arr[N-1-j][i]
            a2[i][j] = arr[N-1-i][N-1-j]
            a3[i][j] = arr[j][N-1-i]
    print(f'#{test_case}')
    for a,b,c in zip(a1, a2, a3):
        print(f'{"".join(a)}{"".join(b)}{"".join(c)}')

#2 전치배열과 읽는 방향에 따른 처리
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    arr_t = list(map(list, zip(*arr)))
    a1 = [[0] * N for _ in range(N)] #90도
    a2 = [[0] * N for _ in range(N)]
    a3 = [[0] * N for _ in range(N)]
    print(f'#{test_case}')
    for i in range(N):
        print(f'{"".join(arr_t[i][::-1])}{"".join(arr[N-1-i][::-1])}{"".join(arr_t[N-1-i][::-1])})



for i(N):
    arr_t[i][::-1]+
    arr[N-1-i][::-1]+
    arr_t[N-1-i]