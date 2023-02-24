import sys

sys.stdin = open("input.txt", "r", encoding='UTF-8')

for t in range(1, 4):
    n, password = map(str, input().split())
    n = int(n)
    password = list(password)
    k = 100
    while k > 0:
        k -= 1
        for i in range(n-1):
            if password[i] == password[i+1]:
                del password[i:i+2]
                n -= 2
                break

    print(f'#{t} {"".join(password)}')

