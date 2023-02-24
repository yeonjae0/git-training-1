import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')


T = int(input())
for t in range(1, T+1):
    str = input()
    stack = []
    top = -1
    print(str)
    for i in range(len(str)):
        if len(stack) == 0:  # 처음엔 무조건 넣어주기
            stack += str[i]
        elif stack[top] == str[i]:  # 같으면 안 넣어주고 pop
            stack.pop()
        else:
            stack += str[i]
    print(f'#{t} {len(stack)}')




