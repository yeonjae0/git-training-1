#SWEA GNS 딕셔너리 버전 (하나씩 value값 빼주기 실패)
import sys
sys.stdin = open("input.txt", "r")

dic = {}
str_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for i in range(10):
    dic[i] = [str_list[i]] #여기에 하나씩 넣어줄 예정
#print(dic)

t = int(input())
for a in range(1, t+1):
    ht = list(input().split())
    case = list(input().split())
    for j in range(10):
        #print(f'dic[j] {dic[j]}')
        for word in case:
            if word == dic[j][0]:
                dic[j].append(word)
        #del dic[j][0]
#여긴 프린트 구역
    print(f'#{a}')
    for ans in dic.values():
        print(*ans, end =' ')
    print()

