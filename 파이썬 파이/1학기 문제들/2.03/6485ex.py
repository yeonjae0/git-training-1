#6485 삼성시의 버스노선 해설

#1. cnts[] 빈도수표시(N개)
#2 지정된 정류장 버스 개수 
# alst = [] p입력 alst.append(cnts[p])

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    
# [1] N번 반복하면서 노선입력, 빈도수 표시
    cnts = [0] * 5001
    for _ in range(N):
        S, E  = map(int, input().split())
        for i in range(S, E+1):
            cnts[i] += 1

    P = int(input())
    alst = []
    for _ in range(P):
        P = int(input())
        alst.append(cnts[p])

    print(f"#{test_case}", *alst)