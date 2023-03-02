# 1065 백준 랜선 자르기
# 이진 탐색 사용

import sys
sys.stdin = open("input(1065).txt")

k, n = map(int, input().split())
lan_lst = [int(input()) for _ in range(k)]

s = 0
g = max(lan_lst)

while s >= g:

