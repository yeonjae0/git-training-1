#swea 9386 연속한 1의 개수 설명

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input()))
    ans = cnt = 0
    for i in range(N):
        if lst[i] == 0:
            cnt = 0
        else:
            cnt += 1
            if ans < cnt:
                ans = cnt



    print(f"#{test_case}", ans)