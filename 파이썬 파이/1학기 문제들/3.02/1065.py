# 1065 백준 랜선 자르기
# 시간 초과
import sys
sys.stdin = open("input(1065).txt")

k, n = map(int, input().split())
lan_lst = [int(input()) for _ in range(k)]

max_n = sum(lan_lst) // n  # 이론상 최대로 길어질 수 있는 랜선 길이
print(max_n)

while True:
    cnt = 0
    for i in range(k):
        cnt += lan_lst[i] // max_n
    if cnt >= n:
        ans = max_n
        break
    else:

        max_n -= 1
print(ans)
