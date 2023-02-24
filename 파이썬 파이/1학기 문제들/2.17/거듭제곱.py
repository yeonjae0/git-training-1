import sys

sys.stdin = open("input.txt", "r", encoding='UTF-8')

def power(n, m):
    if m == 0:
        return 1
    return n * power(n, m-1)


for _ in range(10):
    t = int(input())
    n, m = map(int, input().split())
    #print(n, m)

    print(f'#{t} {power(n, m)}')
