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

i = 0
# 여기서부터 시작
cnt = lst[0][1]  # 높이가 없는 구역의 지붕을 유지
#for i in range(1, max_idx):
while cnt < max_h:
    i += 1
    # 현재 cnt보다 다음 기둥이 크거나 같으면 / 다음 기둥까지 현재 유지
        if cnt <= lst[i][1]:
            for j in range(lst[i-1][0], lst[i][0]):
                height[j] = cnt
            cnt = lst[i][1]
        # 현재 cnt보다 다음 기둥이 작을 때
        elif cnt > lst[i][1]:
            for j in range(lst[i-1][0], lst[i][0]):
                height[j] = cnt
print(height)
cnt = lst[-1][1]
# print(cnt)
# print(len(height))
#for i in range(len(lst)-1, max_idx+1, -1):
i = len(lst) + 1
while cnt < max_h:
    i -= 1
    # 현재 cnt보다 다음 기둥이 크거나 같으면 / 다음 기둥까지 현재 유지
        if cnt <= lst[i][1]:
            print(i)
            for j in range(lst[i-1][0], lst[i][0]):
                height[j] = cnt
            cnt = lst[i][1]
        # 현재 cnt보다 다음 기둥이 작을 때
        elif cnt > lst[i][1]:
            for j in range(lst[i-1][0], lst[i][0]):
                height[j] = cnt

print(height)
# print(lst)
# print(cnt)
print(sum(height))