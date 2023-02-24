import sys

sys.stdin = open("input.txt", "r", encoding='UTF-8')

N = int(input())
dict = {}
for _ in range(N):
    l, h = map(int, input().split())
    dict[l] = h
lst = sorted(dict.items())  # 리스트에 (좌표, 높이) 튜플 형태로 저장
#lst.append((max(lst)[0]+1,0))
height = [0] * (max(lst)[0]+1)
cnt = lst[0][1]  # 높이가 없는 구역의 지붕을 유지
# print(lst)


h_lst = []
i_lst = []
for hh in range(len(lst)):
    if hh == 0:
        max_h = lst[hh][1]
        max_idx = lst[hh][0]
    if lst[hh][1] > max_h:
        max_h = lst[hh][1]
        max_idx = lst[hh][0]



print(max_h)  # 튜플 뒤
print(max_idx)  # 튜플 앞

'''
왼쪽 오른쪽 양쪽에서 포인터
max_h를 만나면 멈추자
'''
i = 0  # lst의 인덱스
while cnt != max_h:

