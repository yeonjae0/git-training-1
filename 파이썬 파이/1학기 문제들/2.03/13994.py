#13994 새로운 버스노선
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(T):
    cnt = [0] * 1001
    N = int(input())
    for i in range(N):
        bus = list(map(int, input().split())) #각 버스를 차례로 받음
        if bus[0] == 1:
            for one in range(bus[1], bus[2]+1):
                cnt[one] += 1
        elif bus[0] == 2:
            for two in range(bus[1], bus[2]+1, 2): #A가 홀수,짝수 여부 상관없이 2칸마다 카운트
                cnt[two] += 1
        else:
            if bus[1] % 2 == 0:
                for three in range(bus[1], bus[2]+1):
                    if three % 4 == 0:
                        cnt[three] += 1
            else:
                for three_ in range(bus[1], bus[2]+1):
                    if (three_ % 3 == 0) and (three_ % 10 != 0):
                        cnt[three_] += 1
    print(f'#{t+1} {max(cnt)}')

