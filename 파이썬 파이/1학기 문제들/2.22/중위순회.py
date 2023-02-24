import sys

sys.stdin = open("input(alpha).txt", "r", encoding='UTF-8')

def in_order(n):
    if n:  # n이 0이 아니면
        in_order(int(data[n][2]))
        print(data[n][1], end='')
        in_order(int(data[n][3]))


for t in range(1, 11):
    N = int(input())
    data = [input().split() for _ in range(N)]
    # 맨 앞에 리스트 한 줄 더 삽입 (노드와 인덱스 맞춰주려고)
    data.insert(0,[0, 0, 0, 0])

    # 글자수 자리 맞춰서 받아주기
    for i in data:
        # 자식이 없거나 하나인 경우, 크기를 맞추자
        while len(i) != 4:
            i.append('0')
# 여기는 프린트 구간
    print(f'#{t}', end=' ')
    in_order(1)  # 루트 정점 번호는 항상 1(문제)
    print()
print(data)