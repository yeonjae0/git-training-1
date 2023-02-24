import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(T):
    N = int(input())
    n_list = list(map(int, input()))
    ans = cnt = 0
    for i in range(N):
        if n_list[i] == 0:
            cnt = 0
        else:
            cnt += 1
            if ans < cnt:
                ans = cnt

    print(f"#{t+1} {ans}")