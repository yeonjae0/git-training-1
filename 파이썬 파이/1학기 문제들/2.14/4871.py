# 4871 swea 그래프 경로
import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')


def dfs(graph, s, g, visited):
    if s == g:
        return 1

    idx = []
    for x in range(E):
        if (graph[x][0] == s) and (visited[s] == False):  # 첫 시작점 찾기
            #visited[s] = True
            #print(graph[x])
            idx.append(graph[x][1])  # 도착 지점을 인덱스에 넣기
            print(idx)

    for i in idx:
        if (visited[i] == False) and (i in idx):  # 해당 노드에 간 적이 없고, 시작값 리스트 내에 있으면
            #print(i)
            tmp1 = []
            for y in range(E):
                tmp1.append(graph[y][1])
                if i not in tmp1: # i가 도착점 리스트에 없으면 (
                # if dfs(graph, i, g, visited) == 0: # 재귀를 돌렸을 때 else로 빠져서 0이 나오면
                    visited[i] = True
                    print(i)
                    continue
        return dfs(graph, i, g, visited)  # 스타트 지점이 인덱스 내 i로 바뀌고 돌아감

    else:
        return 0  # 반복문 끝까지 일치하지 않을 때

T = int(input())
for t in range(1, T + 1):

    V, E = map(int, input().split())
    visited = [False] * (V+1)

    graph = []
    for j in range(E):
        graph.append(list(map(int, input().split())))

    s, g = map(int, input().split())

    print(f'#{t} {dfs(graph, s, g, visited)}')