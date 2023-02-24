# 4874 SWEA Forth

import sys

sys.stdin = open("input.txt", "r", encoding='UTF-8')

T =int(input())
for t in range(1, T+1):
    postfix = input().split()
    stack = []
    k = -1
    try:
        while k != '.':  # 후위표기법 내의 요소를 도는 반복문(인덱스 0부터)
            k += 1

            if postfix[k] == '+':
                stack.append(stack.pop() + stack.pop())
            elif postfix[k] == '-':
                stack.append(stack.pop() - stack.pop())
            elif postfix[k] == '*':
                stack.append(stack.pop() * stack.pop())
            elif postfix[k] == '/':
                rv = stack.pop()
                stack.append(stack.pop() // rv)
            else:
                stack.append(int(postfix[k]))

        if len(stack) > 1: # 제대로 된 코드는 스택 내에 정답 하나만 있어야함
            print(f'#{t} error')

        else:
            print(f'#{t} {stack.pop()}')
        #print(stack)

    except IndexError:  # 계산식에서 pop할 숫자가 없어서 에러날 때
        print(f'#{t} error')