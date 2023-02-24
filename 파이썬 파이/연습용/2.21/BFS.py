# def BFS(G, v):  # G: 그래프, v: 탐색 시작점
#     vistited = [0] *(n+1)
#     queue = []  # 큐 생성
#     queue.append(v)  # 시작점 v를 큐에 삽입
#     while queue:  # 큐가 비어있지 않은 경우
#         t = queue.pop(0)  # 큐의 첫번째 원소 반환
#         if not vistited[t]:  # 방문되지 않은 곳이라면
#             vistited[t] = True  # 방문한 것으로 표시
#             visit(t)  # 정점 t에서 할 일
#             for i in G[t]:  # t와 연결된 모든 정점에 대해
#                 if not vistited[i]:  # 방문되지 않은 곳이라면
#                     queue.append(i)  # 큐에 넣기


def BFS(G, v, n):  # G: 그래프, v: 탐색 시작점
    vistited = [0] *(n+1)
    queue = []  # 큐 생성
    queue.append(v)  # 시작점 v를 큐에 삽입
    visited[v] = 1
    while queue:  # 큐가 비어있지 않은 경우
        t = queue.pop(0)  # 큐의 첫번째 원소 반환
        if not vistited[t]:  # 방문되지 않은 곳이라면
            vistited[t] = True  # 방문한 것으로 표시
            visit(t)  # 정점 t에서 할 일
            for i in G[t]:  # t와 연결된 모든 정점에 대해
                if not vistited[i]:  # 방문되지 않은 곳이라면
                    queue.append(i)  # 큐에 넣기
                    vistited[i] = vistited[n] + 1  # n으로 부터 1만큼 이동