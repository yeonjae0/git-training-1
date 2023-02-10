#SWEA 4865 글자수
import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')

T = int(input())
for t in range(1, T+1):
    str1 = list(set(input()))
    str2 = input() #긴 문자열
    dic = {}
    for i in range(len(str1)):
        dic[str1[i]] = 0 #str1의 요소(알파벳 하나)가 키, 값은 모두 0
        for j in range(len(str2)): #동시에 str2를 돌면서
            if str1[i] == str2[j]: #해당 str1의 알파벳과 str2에 있는 알파벳이 일치할 때마다
                dic[str1[i]] += 1 #+1을 해준다
    print(f'#{t} {max(dic.values())}')
