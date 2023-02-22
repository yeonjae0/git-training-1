import sys
sys.stdin = open("input(alpha).txt", "r", encoding='UTF-8')

N = int(input())
data = [input().split() for _ in range(N)]



data.insert(0,[0, 0, 0, 0])

for i in data:
    # 자식이 없거나 하나인 경우, 크기를 맞추자
    while len(i) != 4:
        i.append('0')
print(data)