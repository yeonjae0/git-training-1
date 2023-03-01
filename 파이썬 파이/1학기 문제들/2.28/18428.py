import sys
sys.stdin = open("input(18428).txt")
'''
t_lst의 각 인덱스를 대상으로 각각 2차원 리스트를 만들기
t1 = [[상],[하],[좌],[우]]  if 방향대로 검사했을 때 S가 있을 경우 해당 S가 있을 때까지의 좌표 해당 방향에 넣기
*바꿈* t_posi_lst = [ [] for _ in range(len(t_lst) * 4)
t숫자 리스트들을 total_t에 넣고 중복값 찾기 / 해당 값이 있는 리스트 안 리스트 자체를 전부 삭제
3 - 삭제한 값(좌표 개수) 보다 비어있지 않은 리스트가 많으면 NO / 적으면 YES
'''
# teacher 하나의 좌표를 받아서 사방을 검사해주는 함수를 만들어볼까
def monitor(teacher, t_posi_lst):
# 위 (teacher는 좌표)
    t = 0  # 인덱스 옮겨줄 포인터
    # posi = teacher[0]
    while teacher[0] != 0 or ((teacher[0] - t, teacher[1]) not in s_lst):
        t += 1
        t_posi_lst[0].append((teacher[0] - t, teacher[1]))
# 없으면 t 한 만큼 pop하기



N = int(input())
arr = [list(map(str, input().split())) for _ in range(N)]
print(arr)
t_lst = []  # 선생님의 좌표를 넣어놓을 리스트
s_lst = []  # 학생의 좌표를 넣어놓을 리스트
# 리스트에 값을 넣어주기 위한 리스트
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'T':
            t_lst.append((i, j))
        elif arr[i][j] == 'S':
            s_lst.append((i, j))
print(t_lst)
print(s_lst)
t_posi_lst = [ [] for _ in range(len(t_lst) * 4)]
print(t_posi_lst)
#for teacher in t_lst:  # 선생님의 수 만큼

