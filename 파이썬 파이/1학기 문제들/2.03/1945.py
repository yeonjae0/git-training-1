#1945 간단한 소인수분해

import sys
sys.stdin = open("input.txt", "r")

lst = [2, 3, 5, 7 ,11]
T = int(input())

for a in range(T):
    cnt = [0] * len(lst) #각각으로 나눠지는 만큼 넣어주기 때문에 lst의 길이만큼
    N = int(input())

    for i in range(len(lst)):
        while N % lst[i] == 0:
            cnt[i] += 1
            N = N // lst[i]

    print(f'#{a+1}', *cnt)
