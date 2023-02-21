# 5105 SWEA 미로의 거리
# 0통로 1벽 2출발 3도착
import sys
sys.stdin = open("input.txt", "r")

def bfs(i, j):
    visited = [[0] * n for _ in range(n)]
    global graph
    global ans
    queue = []
    di = [-1, 1, 0, 0]  # 상하좌우
    dj = [0, 0, -1, 1]
    queue.append((i, j))
    visited[0][j] = 1

    while queue:
        i, j = queue.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if (ni < 0) or (nj < 0) or (ni >= n) or (nj >= n):  # 범위 밖
                continue

            elif (graph[ni][nj] == 0) and (visited[ni][nj] == 0):  # 길을 찾아가는 중
                queue.append((ni, nj))
                graph[ni][nj] = graph[i][j] + 1
                visited[ni][nj] = 1

            if graph[ni][nj] == 2:  # 도착점 찾음
                ans.append(graph[i][j] - 3)  # ans 값만 넣어주고 리턴은 안함

T = int(input())
for t in range(1, T+1):
    n = int(input())
    graph = [list(map(int, input())) for _ in range(n)]

    for x in range(n):  # 스타트 지점의 좌표(인덱스)를 찾기 위한 반복문
        for y in range(n):
            if graph[x][y] == 3:
                si, sj = x, y
    ans = []
    bfs(si, sj)
    if not ans:
        print(f'#{t} 0')
    else:
        print(f'#{t} {min(ans)}')