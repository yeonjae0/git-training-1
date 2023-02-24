# 1238 SWEA Contac

import sys

sys.stdin = open("input.txt", "r", encoding='UTF-8')

def bfs(start):
    q = []  # 큐 생성. 재귀가 호출될 때마다 비는건가?
    visited = [0] * 101  # 방문했던 곳인지 판별


for t in range(1, 11):
    l, start = map(int, input().split())
    lst = list(map(int, input().split()))
    arr = [[] for _ in range(101)]  # 인덱스 번호가 본인 숫자, 인덱스에 할당된 값이 전화 거는 곳

    # arr에 연결 정보 넣어줌
    for i in range(0,l,2):
        s, e = lst[i], lst[i+1]
        arr[s].append(e)
    #print(arr)
