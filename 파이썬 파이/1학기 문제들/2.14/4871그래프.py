# 4871 swea 그래프 경로
import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')

T = int(input())
for t in range(1, T + 1):

    V, E = map(int, input().split())
    visited = [False] * (V+1)

    graph = []
    for j in range(E):
        graph.append(list(map(int, input().split())))

    s, g = map(int, input().split())

    for i in range()