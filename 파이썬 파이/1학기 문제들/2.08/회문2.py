import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')

testcase = int(input())
for t in range(1, testcase+1):
    n, m = map(int, input().split()) #n*n 문자열에서 길이 m 회문 찾기
    case = [] #여기 리스트로 회문 들어있음
    word = ''
    ans = '' #여기 답을 넣어주자
    for _ in range(n):
        case.append(input())

    # 가로로 확인
    for i in range(n):
        for j in range(n-m+1):
            word = case[i][j:m+j]
            #print(f'가로 {word}')
            #print(word[::-1])
            if word == word[::-1]:
                ans = word

    #세로로 확인
    clone = []#인덱스를 바꾼 문자열을 넣어줄 리스트 (그냥 하면 나중에 오류)
    for a in range(n):
        row = []
        for b in range(n):
            row.append(case[b][a])#열 별로 따로 묶어주고
        clone.append(''.join(row)) #조인으로 묶어준 로우를 넣어주기
    #print(clone)
    if len(ans) == 0:
        for k in range(n):
            for l in range(n-m+1):
                word = clone[k][l:m+l]
                #print(f'가로 {word}')
                if word == word[::-1]:
                    ans = word

    print(f'#{t} {ans}')