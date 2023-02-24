#6019 기차 사이의 파리
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(T):
    D, A, B, F = map(int, input().split())
    print(f'#{t+1} {F * D/(A + B)}')


