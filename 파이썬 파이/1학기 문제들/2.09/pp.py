import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')

def bf(st, case,n, m):
    cnt = 0
    for i in range(n-m+1):
        for j in range(m):
            if case[i+j] != st[j]:
                pass
            else:
                cnt += 1
    return cnt

for t in range(1, 11):
    st = input() #패턴
    case = input() #전체 문자열
    m = len(st)
    n = len(case)
    print(bf(st, case,n, m))


