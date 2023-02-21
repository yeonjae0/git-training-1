# 5097 SWEA 회전
import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    for i in range(M):
        lst.append(lst.pop(0))  # 앞의 숫자를 빼서 뒤에 계속 넣어준다.
    print(f'#{t} {lst[0]}')
