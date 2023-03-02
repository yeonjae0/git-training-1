# 14696 백준 딱지놀이
import sys
sys.stdin = open("input(14696).txt")

T = int(input())
for _ in range(T):
    A = list(map(int, input().split()))
    del A[0]
    a_lst = [0] * 5
    B = list(map(int, input().split()))
    del B[0]
    b_lst = [0] * 5

    for i in A:  # 리스트의 숫자에 해당하는 인덱스에 +1씩
        a_lst[i] += 1
    for j in B:
        b_lst[j] += 1
    for k in range(4, 0, -1):
        if a_lst[k] > b_lst[k]:
            print('A')
            break
        elif a_lst[k] < b_lst[k]:
            print('B')
            break
    if a_lst == b_lst:  # 숫자가 전부 같으면
        print('D')

