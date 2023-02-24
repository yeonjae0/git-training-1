# a = 'car'
# print(a[::-1]) #rac
import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')

t = int(input())
for a in range(1, t+1):
    n, m = map(int, input().split())
    case = [] #여기 2차원 리스트로 회문 들어있음
    word = ''
    ans = '' #여기 답을 넣어주자
    for _ in range(n):
        case.append(list(input().split()))
    #print(case)
    for i in range(n): #가로로 확인
        for j in range(n-m+1):
            word = case[i][j:m+j]
            #print(word)
            #print(word[::-1])
            if word[0] == word[0][::-1]: #word가 리스트라서
                ans = word[0]
    # for i in range(n):
    print(ans)




