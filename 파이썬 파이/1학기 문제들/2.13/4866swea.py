import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')

T = int(input())
for t in range(1, T+1):
    str = list(input())  # 문자열 넣어주기
    lst = ['(', ')', '{', '}']

    stack = []
    top = -1
    for i in str:
        if (len(stack) == 0) and (i in lst):  # 인덱스 에러 방지/ 첫 괄호 무조건 넣기
            stack.append(i)

        elif (len(stack) != 0) and (stack[top] == '(') and (i == ')'):
            stack.pop()

        elif (len(stack) != 0) and (stack[top] == '{') and (i == '}'):
            stack.pop()

        elif i in lst:  # 지워지지 않는 괄호는 스택에 넣어주기
            stack.append(i)

    if len(stack) == 0:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')
