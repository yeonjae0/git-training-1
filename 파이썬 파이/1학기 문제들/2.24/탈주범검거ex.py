# 1953 SWEA 탈주범 검거

import sys

sys.stdin = open("input.txt", "r", encoding='UTF-8')

p = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
opp = {0: 1, 1: 0, 2: 3, 3: 2}
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(si, sj, L):
    q = []  # [0]
    v = [[0] * M for _ in range(N)]  # 가로 세로 다를때 특히 주의!!!!

    q.append((si, sj))
    v[si][sj] = 1
    cnt = 1

    while q:
        ci, cj = q.pop(0)
        if v[ci][cj] == L:
            return cnt

        for dr in p[arr[ci][cj]]:  # 현재위치 파이프에 연결된 방향 하나씩 처리
            ni, nj = ci + di[dr], cj + dj[dr]
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and \
                    opp[dr] in p[arr[ni][nj]]:  # 내 방향으로 연결된 파이프가 이동할 방향에 있다면..
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
                cnt += 1
    # 이 경우 -1값을 리턴???
    # 공간이 좁아서 L일전에 모두 방문!
    return cnt


T = int(input())
for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = bfs(R, C, L)
    print(f'#{test_case} {ans}')