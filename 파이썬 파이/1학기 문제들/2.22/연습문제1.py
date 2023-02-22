import sys

sys.stdin = open("input(ex).txt", "r", encoding='UTF-8')

def pre_order(n):
    if n > 0:
        print(n, end=' ')
        pre_order(left[n])
        pre_order(right[n])

v = int(input())
e = v - 1

edge = list(map(int, input().split()))

left = [0] * (v + 1)    # 부모 인덱스로 왼쪽 자식 번호 저장
right = [0] * (v + 1)   # 부모 인덱스로 오른쪽 자식 번호 저장
parent = [0] * (v + 1)  # 자식 인덱스로 부모 번호 저장

# root 선언
root = 0
for i in range(e):
    p1, c1 = edge[i * 2], edge[i * 2 + 1]   # 부모, 자식

    if not left[p1]:    # 왼쪽 자식 없을 때
        left[p1] = c1   # 부모 인덱스로 자식 번호 저장
    else:   # 있을 때
        right[p1] = c1
    parent[c1] = p1 # 자식 인덱스로 부모 저장

for i in range(1, v + 1):
    if not parent[i]:
        root = i
        break

pre_order(1)
#print()
