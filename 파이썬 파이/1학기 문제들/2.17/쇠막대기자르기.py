import sys

sys.stdin = open("input.txt", "r", encoding='UTF-8')

T = int(input())
for t in range(1, T+1):
    bracket = input()
    ans = 0  # 답을 넣어줄 변수
    cnt = 0  # 현재까지 존재하는 쇠막대기의 개수
    for i in range(len(bracket)-1):
        if bracket[i] == '(':
            if bracket[i+1] == ')':  # 레이저
                ans += cnt
            else:  # 쇠막대기 시작
                cnt += 1
        else:  # bracket[i] == ')'
            if bracket[i-1] == '(':  #레이저일 경우 무시
                pass
            else:  # 쇠막대기 닫음
                cnt -= 1
                ans += 1
    ans += 1  # i가 가지 못하는 마지막 괄호
    print(f'#{t} {ans}')


# 테케 하나 오답