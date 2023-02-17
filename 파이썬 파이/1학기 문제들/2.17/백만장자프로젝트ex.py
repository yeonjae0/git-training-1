'''
시간과 메모리를 줄일 수 있는 방법
-뒤부터 검사
작은값 -> 차이
큰값 -> 최대값 갱신

for n in lst[::-1]:
    if mx > n:
        ans += mx - n
    else:
        mx = n
'''


import sys

sys.stdin = open("input.txt", "r", encoding='UTF-8')
# # 앞부터 찾기
# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     lst = list(map(int, input().split()))
#
#     i = ans = 0
#     while i < N:
#         # [1] i ~ 끝까지 최대값의 index 찾기
#         i_mx = i
#         for j in range(i+1, N):
#             if lst[i_mx] < lst[j]:
#                 i_mx = j
#         # [2] i ~ i_mx 까지의 최대값과의 차이 누적
#         for j in range(i, i_mx):
#             ans += lst[i_mx] - lst[j]
#
#         i = i_mx + 1
#     print(f'#{test_case} {ans}')

# 뒤쪽부터 찾는 방법
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))[::-1]

    ans = mx = 0
    for n in lst:
        if mx > n:
            ans += mx - n
        else:
            mx = n
    print(f'#{test_case} {ans}')