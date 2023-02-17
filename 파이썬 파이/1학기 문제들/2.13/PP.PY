t = int(input())

def erase(s):
    stack = []
    # index error 방지 위해 첫 글자를 채워준다.
    stack.append(s[0])
    for i in range(1, len(s)):
        if stack != 0:
            if stack[-1] != s[i]:
                stack.append(s[i])
                #print(stack)
            else:
                stack.pop()
    return stack

for case in range(1, t+1):
    print(f'#{case}', erase(input()))