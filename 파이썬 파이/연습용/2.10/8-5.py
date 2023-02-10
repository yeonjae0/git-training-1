import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')

#인풋 받고 화폐 가치는 리스트로 정리
n, m = map(int, input().split())
money_list = []
for _ in range(n):
    money_list.append(int(input()))
#print(money_list)

d = [0] * (m+1)
d[0] = 999999
#확인할 돈(m)만큼 반복문을 돌린다.
for i in range(2, m+1):
    for j in money_list:
        if (i - j != 0):
            d[i] = min([d[i], d[i-j]+1])
            d[i] += 1
        else:
            d[i] = d[0]

#답을 내보자
if d[m] == d[0]:
    print(-1)
else:
    print(d[m])
