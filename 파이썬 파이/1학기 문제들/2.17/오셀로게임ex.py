# 14133 SWEA  재미있는 오셀로 게임

'''
범위 x => padding 0으로 숫자를 넣기
[1] 초기모양 배치
[2] arr[si][sj] = d
8방향 뻗어나가면서
arr[ni][nj]
0: break
다른 돌: 후보(좌표) tlst 추가
같은 돌: tlst 후보들 뒤집기


'''

import sys

sys.stdin = open("input.txt", "r", encoding='UTF-8')

T = int(input())
for test_case in range(1, T+1):
    N,M = map(int, input().split())
    # arr 네 방향 0으로 패딩해서 둘러쌈
    arr = [[0] * (N+2) for _ in range(N+2)]
    # [1] 초기 돌 위치 놓기
    m = N // 2
    arr[m][m] = arr[m+1][m+1] = 2
    arr[m+1][m] = arr[m][m+1] = 1
    # [2] 흑돌 백돌 입력 받아서 처리
    for _ in range(M):
        si, sj, d = map(int, input().split())
        arr[si][sj] = d  # 돌 놓기
        # 8방향 처리
        for di, dj in ((-1,-1), (-1, 0),(-1,1), (0,-1), (0,1 ),(1,-1),(1,0),(1, 1)):
            # 해당 방향으로 뻗어나가면서 처리
            tlst = []
            for mul in range(1, N):
                ni, nj = si+di*mul, sj+dj*mul
                if arr[ni][nj] == 0:  # 빈칸 번위 밖
                    break
                elif arr[ni][nj] != d:  # 다른 돌인 경우 뒤집기 후보에 추가
                    tlst.append((ni, nj))
                else:  # 같은돌 => 후보들을 뒤집고, 종료
                    while tlst:
                        ti, tj = tlst.pop()
                        arr[ti][tj] = d
                    break

    bcnt = wcnt = 0
    for lst in arr:
        bcnt += lst.count(1)
        wcnt += lst.count(2)
    print(f'#{test_case} {bcnt} {wcnt}')