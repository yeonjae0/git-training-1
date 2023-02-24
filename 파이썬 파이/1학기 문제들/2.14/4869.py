# 4869 swea 종이붙이기
import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')

T = int(input())
for t in range(1, T+1):
    n = int(input()) // 10
    d = [0] * (n+1)
    d[1] = 1
    d[2] = 3
    for i in range(3,n+1):
        d[i] = d[i-1] + 2*d[i-2]  # n=1 짜리 종이 2개로 붙인 경우와(눕힌), 정사각형 하나
    print(f'#{t} {d[n]}')

