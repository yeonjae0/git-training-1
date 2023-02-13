import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')

T = int(input())
for t in range(1, T+1):
    n = int(input())
    stack = [0] * n
    top = -1

