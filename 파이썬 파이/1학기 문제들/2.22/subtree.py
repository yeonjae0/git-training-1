# swea 5174 subtree
import sys

sys.stdin = open("input.txt", "r", encoding='UTF-8')

def subtree(N):  # N은 루트
    #global tree
    global cnt
    if N > 0:
        cnt += 1
        #print(f'tree[N][0] {tree[N][0]}')
        subtree(tree[N][0])
        #print(f'tree[N][1] {tree[N][1]}')
        subtree(tree[N][1])

    # elif (tree[N][1] > 0) and (N > 0):
    #     cnt += 1
    else:
        #cnt += 1
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
        if not tree[p][0]: # left 기록 x -> 기록하기
            tree[p][0] = c
        else:
            tree[p][1] = c
        tree[c][2] = p

    print(tree)
    print(subtree(N))