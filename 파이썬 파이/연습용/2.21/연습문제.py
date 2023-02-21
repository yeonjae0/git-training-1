"""
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""
def bfs(v, N):
    # visited 생성
    # 큐 생성
    # 시작점 인큐
    # 시작점 인큐 표시
    visited = [0] * (N+1)
    q = [v]

    visited[v] = 1
    while q:  # q가 비어있지 않으면
        t = q.pop(0)  # 디큐
        print(t, end=' ')  # t에서 처리할 일
        for j in adjL[t]:  # t에 인접이고 방문한 적 없는 v
            if visited[j] == 0:
                q.append(j)  # v 인큐
                visited[j] = visited[t] + 1  # v 인큐되었음 표시


V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjL = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjL[n1].append(n2)
    adjL[n2].append(n1)

bfs(1, V)  # 시작정점1, 마지막정점 V
