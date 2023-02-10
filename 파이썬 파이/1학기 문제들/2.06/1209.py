#swea 1209 Sum
import sys
sys.stdin = open("input.txt", "r")

for _ in range(1, 11):
    t = int(input())
    graph =[]
    slst = [] #sum_n 들의 값을 넣어줄 리스트
    sum_n = 0 #sum_n 값 초기화에 주의
    for _ in range(100):
        graph.append(list(map(int, input().split())))
#시작
    for i in range(100): #행 위주로 가로로 쭉쭉 더해주기
        for j in range(100):
            sum_n += graph[i][j]
        slst.append(sum_n)
        sum_n = 0
    for j in range(100): #열 위주로 세로로 쭉쭉 더해주기
        for i in range(100):
            sum_n += graph[i][j]
        slst.append(sum_n)
        sum_n = 0
    for k in range(100): # 오른쪽 대각선으로
        sum_n += graph[k][k]
    slst.append(sum_n)
    sum_n = 0
    for n in range(100): #왼쪽 대각선으로
        sum_n += graph[n][99-n]
    slst.append(sum_n)
    sum_n = 0

    print(max(slst))




