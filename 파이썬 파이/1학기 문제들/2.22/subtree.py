# swea 5174 subtree
import sys

sys.stdin = open("input.txt", "r", encoding='UTF-8')

def subtree(N):  # N은 루트
    global cnt
    if N > 0:
        cnt += 1
        subtree(tree[N][0])
        subtree(tree[N][1])

    # elif (tree[N][1] > 0) and (N > 0):
    #     cnt += 1
    return cnt

T = int(input())
for t in range(1, T+1):
    E, N = map(int, input().split())
    edge = list(map(int, input().split()))
    cnt = 0

    tree = [[0 for _ in range(3)] for _ in range(E+2)]
    for i in range(E):  # 간선의 수만큼
        p, c = edge[i * 2], edge[i * 2 + 1]

        # [0, 0, 0] -> 0: left, 1: right, 2: parent
        if not tree[p][0]:  # left 기록 x -> 기록하기
            tree[p][0] = c
        else:
            tree[p][1] = c
        tree[c][2] = p


    print(f'#{t} {subtree(N)}')

# cnt 계속 None으로 print되는 문제가 생겼었음
# 이럴 때는 함수 호출하고 그 아래에 print(cnt)
# print(cnt) ->  global cnt None 값 나올 때 사용 !!!