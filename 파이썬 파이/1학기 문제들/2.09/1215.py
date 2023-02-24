for t in range(1, 11):
    n = int(input()) #찾아야 하는 회문의 길이
    case = [] #여기에 회문을 받아주자
    word = ''
    cnt = 0
    for _ in range(8):
        case.append(input())
    #가로로 확인
    for i in range(8):
        for j in range(9-n):
            word = case[i][j:n+j]
            if word == word[::-1]:
                cnt += 1
    #세로를 확인하기 위한 클론 만들기
    clone = []
    for a in range(8):
        row = []
        for b in range(8):
            row.append(case[b][a])
        clone.append(''.join(row))
    print(clone)
    #세로 확인하기
    for k in range(8):
        for l in range(9-n):
            word = clone[k][l:l+n]
            if word == word[::-1]:
                cnt += 1
    #print(f'#{t} {cnt}')
