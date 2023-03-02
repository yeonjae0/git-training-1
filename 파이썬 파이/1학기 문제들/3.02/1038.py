# 1038 백준 감소하는 수
# 시간 초과

import sys
sys.stdin = open("input(1038).txt")


def dec_num(num):  # 숫자를 문자열로 변화한 길이만큼 반복문 돌리고 각 한 자리마다 검사
    for j in range(len(str(num)) - 1):
        if int(str(num)[j]) <= int(str(num)[j + 1]):
            return 0
    lst.append(num)
    return 1


N = int(input())
i = 0
lst = []

if N == 0:
    print(0)
    exit()
elif N > (2**10) -1:
    print(-1)
    exit()

while True:
    i += 1
    if i in range(1, 10):
        lst.append(i)
    else:
        dec_num(i)
    if N <= len(lst):
        break

print(lst[N-1])
