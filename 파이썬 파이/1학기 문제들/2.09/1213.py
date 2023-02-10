#swea 1213 string
import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')

for t in range(1, 11):
    tc = int(input())
    st = input()
    case = input() #전체 문자열
    i = 0
    cnt = 0
    while i <= len(case)-1:
        if case[i:i+len(st)] == st:
            cnt +=1
        i += 1
    print(f'#{tc} {cnt}')












    # for i in range(len(case)):
    #     if st[0] == case[i]:
    #         cnt = 0
    #         for j in range(len(st)):
    #             if st[j] == case[i+j]:
    #                 cnt += 1
    #                 if cnt == len(st):
    #                     ans += 1
    # print(ans)



