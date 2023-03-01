import sys
sys.stdin = open("input(18428).txt")
from itertools import combinations
'''
1) 4 방향을 체크할 함수
2) 선생님의 수만큼 검사해서 답을 반환할 함수
( T의 수가 더 적기 때문에 teacher 기준으로 검사)
'''
# def def check_4(x, y, N, obstacle):  # t_lst 중 하나의 x, y좌표 / N / 장애물 콤비네이션 조합
#     if
#
# def ans_return(N):
#     for obstacle in obstacles:
#         cnt = 0
#         for teacher in t_lst:
#             if check_4(teacher[0], teacher[1], N, obstacle):




# 인풋받고 arr만들기
N = int(input())
arr = [list(map(str, input().split())) for _ in range(N)]
print(arr)
arr_ = list(map(list, zip(*arr)))
print(arr_)

# 리스트에 값들 넣어주기
t_lst = []  # 선생님의 좌표를 넣어놓을 리스트
s_lst = []  # 학생의 좌표를 넣어놓을 리스트
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'T':
            t_lst.append((i, j))
        elif arr[i][j] == 'S':
            s_lst.append((i, j))

x_coordinates = [(i, j) for i in range(N) for j in range(N) if arr[i][j] == 'X']
obstacles = list(map(list, combinations(x_coordinates, 3)))  # 장애물 위치 3개씩 묶인 리스트

