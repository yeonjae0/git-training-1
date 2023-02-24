# V:정점  E: 간선
V, E = map(int, input().split())

arr = [[0] * (V+1) for _ in range(V+1)]

for _ in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    arr[n1][n2] = 1  # n1과 n2는 인접해있다.

# 탐색해보기
def dfs(v):
    visited[v] = 1
    print(v, end = " ")
    # 현재 v는 시작정점, 인접한 정점 중 방문을 안한 곳
    for w in range(1, V+1):
        if arr[v][w] == 1 and visited[w] == 0:
            dfs(w)
dfs(1)