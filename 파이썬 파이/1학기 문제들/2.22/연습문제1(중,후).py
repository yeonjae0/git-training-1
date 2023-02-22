'''
1번 노드
- 왼쪽
- 오른쪽
- 부모
'''
# 연습문제1을 중위와 후위로

import sys
sys.stdin = open('input(ex).txt')

def in_order(n):
    if n:
        # print(1234)
        in_order(tree[n][0])
        print(n, end=' ')
        in_order(tree[n][1])

def post_order(n):
    if n:
        post_order(tree[n][0])
        post_order(tree[n][1])
        print(n, end=' ')

v = int(input())
e = v - 1

edge = list(map(int, input().split()))

tree = [[0 for _ in range(3)] for _ in range(v+1)]
for i in range(e):
    p2, c2 = edge[i * 2], edge[i * 2 + 1]

    # [0, 0, 0] -> 0: left, 1: right, 2: parent
    if not tree[p2][0]: # left 기록 x -> 기록하기
        tree[p2][0] = c2
    else:
        tree[p2][1] = c2
    tree[c2][2] = p2

#in_order(1)

print(tree)