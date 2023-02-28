import sys
sys.stdin = open("input.txt", "r")

dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

T = int(input())
for tc in range(1, T+1):
    N, hex_num = map(str, input().split())
    ans = []  # 여기다가 2진수를 담아주자
    tmp1 = 0  # 2진수로 만들어주는 과정에서 사용할 변수
    tmp2 = 0
    tmp3 = 0
    N = int(N)
    for i in range(N):
        try:
            if int(hex_num[i]) == 0:
                ans.append('0'.zfill(4))  # zfill함수
            elif int(hex_num[i]) in range(1, 10):  # 숫자일 경우
                #print(hex_num[i])
                ans.append(int(hex_num[i]) // 2**3)
                tmp1 = int(hex_num[i]) % 2**3
                ans.append(tmp1//2**2)
                tmp2 = tmp1 % 2**2
                ans.append(tmp2//2**1)
                tmp3 = tmp2 % 2**1
                ans.append(tmp3//2**0)
        # elif hex_num[i] in dic:
        except ValueError:  # 문자라서 에러가 날 경우
            # print(dic[hex_num[i]])
            ans.append(dic[hex_num[i]] // 2 ** 3)
            tmp1 = dic[hex_num[i]] % 2 ** 3
            ans.append(tmp1 // 2 ** 2)
            tmp2 = tmp1 % 2 ** 2
            ans.append(tmp2 // 2 ** 1)
            tmp3 = tmp2 % 2 ** 1
            ans.append(tmp3 // 2 ** 0)
    print(f'#{tc}', end=' ')
    for k in range(len(ans)):
        print(ans[k], end='')
    print()
