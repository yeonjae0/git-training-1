# 9489 SWEA 고대유적
"""
# 사용변수 위치/ 초기값
mx = 2
for lst in arr:
    cnt = 0
    for n in lst:
        if n == 1:
            cnt+=1
            if mx < cnt:
                mx = cnt
        else:
            cnt = 0

    count(arr), count(arr_t)
"""
import sys

sys.stdin = open("input.txt", "r", encoding='UTF-8')

def count(arr):
    mx = 2  # 구조물의 최소 크기
    for lst in arr:
        cnt = 0
        for n in lst:
            if n == 1:
                cnt += 1
                if mx < cnt:
                    mx = cnt
            else:
                cnt = 0
    return mx

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    arr_t = list(map(list, zip(*arr)))
    #print(arr_t)
    ans = count(arr)
    t = count(arr_t)
    if ans < t:
        ans = t
    print(f'#{test_case} {ans}')