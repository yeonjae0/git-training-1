import sys
sys.stdin = open("input(18428).txt")
from itertools import combinations

N = int(input())
arr = [list(map(str, input().split())) for _ in range(N)]
print(arr)

t_lst = []  # 선생님의 좌표를 넣어놓을 리스트
s_lst = []  # 학생의 좌표를 넣어놓을 리스트
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'T':
            t_lst.append((i, j))
        elif arr[i][j] == 'S':
            s_lst.append((i, j))
print(t_lst)
print(s_lst)

# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 4방향을 검사.
def check_4(coor):
    for pointer in range(4):
    ni = i+ di[k]


# 리스트에 값을 넣어주기 위한 리스트
posi = [(i, j) for i in range(N) for j in range(N) if arr[i][j] == 'X']
posi_combi = list(combinations(posi, 3))
#print(len(posi_combi))  969
print(posi_combi)
print(posi_combi[0][0])

for combi in posi_combi:
    # arr[combi[0][0]][combi[0][1]] = 'O'
    # arr[combi[1][0]][combi[1][1]] = 'O'
    # arr[combi[2][0]][combi[2][1]] = 'O'
    for teacher in t_lst:  # teacher는 (0 , 6) 같은 형식
        # 좌 우
        left = 0  # 좌측 거리를 더해줄 변수
        right = 0
        cnt = 0  # 0인 상태로 보존되면 정답
        while True:  # 좌측 검사
            # 벽에 닿았거나 장애물 만났으면 다음 방향 검사로 넘어가야함
            if (teacher[0]+left, teacher[1]) in combi or (teacher[0]+left < 0):

            # 학생을 만났다면 반복문을 끝내고 다음 콤비 검사
            elif (teacher[0]+left, teacher[1]) in s_lst:
                cnt += 1
                break
            left += 1


