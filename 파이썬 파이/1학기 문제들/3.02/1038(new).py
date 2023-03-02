# 1038 백준 감소하는 수

import sys
sys.stdin = open("input(1038).txt")
from itertools import combinations

N = int(input())
i = 0
lst = []

if N > 1022:
    print(-1)

else:
    combi_lst = []
    num = list(map(int, range(0, 10)))
    for i in range(1, 11):
        for j in combinations(num, i):
        # combi_lst.append(''.join(combinations(num, i)))
            tmp = sorted(list(j), reverse=True)
            # print(tmp)
            combi_lst.append(int(''.join(map(str, tmp))))
            # combi_lst.append(''.join(j), reversed=True)
        combi_lst.sort()

    # print(combi_lst)

    print(combi_lst[N])
#print(len(combi_lst))