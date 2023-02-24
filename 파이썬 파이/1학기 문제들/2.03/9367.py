#점점커지는 당근의 개수

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for a in range(T):
    N = int(input())
    carrots = list(map(int, input().split()))
    cnt = 1
    ans = 1
    for i in range(len(carrots)-1):
        if carrots[i+1] > carrots[i]:
            cnt += 1
            ans = cnt
        else:
            cnt = 1
    print(f'#{a+1} {ans}')