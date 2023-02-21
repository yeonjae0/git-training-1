# 5105 SWEA 미로의 거리
# 0통로 1벽 2출발 3도착
import sys
sys.stdin = open("input.txt", "r")

def bfs(i, j):
    visited = [[0] * n for _ in range(n)]
    global graph
    global ans
    queue = []
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    queue.append((i, j))
    visited[0][j] = 1
    k = 0
    while graph[i][j] != 2:
    #while queue:
        i, j = queue.pop(0)
        ni = i + di[k]
        nj = j + dj[k]
        # i += di[k]
        # j += dj[k]
        if (ni < 0) or (nj < 0) or (ni >= n) or (nj >= n):  # 범위 밖
            queue.append((i, j))
            k = (k + 1) % 4
            #print(graph)
            continue

        elif (graph[ni][nj] == 0) and (visited[ni][nj] == 0):  # 길을 찾아가는 중
            graph[ni][nj] = graph[i][j] + 1
            visited[ni][nj] = 1
            queue.append((ni, nj))
            k = (k + 1) % 4
            #print(ni, nj)
            #print(graph)
        else:  #  벽에 닿았을 때
            queue.append((i, j))
            k = (k + 1) % 4
            #print(graph)
        if graph[ni][nj] == 2:  # 도착점 찾음
            ans = graph[i][j] - 3
            break
    return print(ans)

T = int(input())
for t in range(1, T+1):
    n = int(input())
    graph = [list(map(int, input())) for _ in range(n)]
    #print(graph)
    for x in range(0, n):
        if graph[0][x] == 3:
            start_j = x
    ans = 0
    #print(type(start_j))
    #print(ans)
    bfs(0, start_j)