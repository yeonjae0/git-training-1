# 5432 SWEA 쇠막대기 자르기
'''
쌓여있는 막대기 수 cnt
if '(' : cnt +=1 레이저 시작?
앞 뒤를 체크 index 사용
else: ')'
    if  st[i-1] == '('  레이저
    else ')' 막대기 끝
    cnt -=1 ans +=1
'''
import sys

sys.stdin = open("input.txt", "r", encoding='UTF-8')

T = int(input())
for test_case in range(1, T+1):
    cnt = 0
    st = input()
    ans = 0
    for i in range(len(st)):  # 막대기 시작 또는 레이저
        if st[i] == '(':  # 기본적으로 '('를 막대기 시작이라고 생각
            cnt += 1
        else:   # ')' 바로 앞의기호를 검사
            cnt -= 1  # 여는 괄호가 아니면 막대기 끝
            if st[i-1] == '(':  # 레이저
                ans += cnt  # 여는 괄호가 레이저면 그 이전의 막대기 개수 만큼 답에 더해줌
            else:  # 막대기의 끝
                ans += 1
    print(f'#{test_case} {ans}')
