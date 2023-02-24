import sys
sys.stdin = open("input.txt", "r")

di = [0, 0, -1, 1] #상하좌우
dj = [-1, 1, 0, 0]
T = int(input())
for a in range(T):
    N = int(input())
    graph = []
    ans = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    #print(graph)
    for i in range(N): #행
        for j in range(N): #열
            for k in range(4):  #상하좌우 움직임
                ni, nj = i +di[k], j +dj[k]
                #print(ni, nj)
                if (0 <= ni < N) and (0 <= nj < N):
                    # print(f'{ni} {nj}')
                    # print(f'{i} {j}')
                    ans.append(abs(graph[i][j] - graph[ni][nj]))
                    #print(abs(graph[i][j] - graph[ni][nj])
    print(sum(ans))