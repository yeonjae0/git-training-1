#swea 1201 Ladder
import sys
sys.stdin = open("input.txt", "r")

for _ in range(10):
    t = int(input())
    ladder = [] #사다리 전체를 2차원 리스트로 받기
    clone = []
    end = 0 #도착 지점의 인덱스 값 넣기 ladder[99][end]
    for _ in range(100):
        ladder.append(list(map(int, input().split())))
        clone.append([[0]*100])

    #end값을 찾기 위한 반복문
    for a in range(100):
        if ladder[99][a] == 2:
            end = a
    #i를 한 번씩 -1
    i = 98 #위로 위로
    while i >= 0:

        if (end-1 >= 0) and (ladder[i][end-1] > 0) and (clone[i][end - 1] == 0):#좌
            clone[i][end-1] += 1
            end = end - 1

        elif (end+1 <= 99) and (ladder[i][end+1] > 0) and (clone[i][end + 1] == 0): #우
            clone[i][end + 1] += 1
            end = end + 1
        else:
            i -= 1
            #print(i)
    print(end)





    #시작 델타버전
    # di = [0, 0, -1] #좌,우,위
    # dj = [-1, 1, 0]
    # i = 98
    # j = end
    # ni = i +
    # while True:
    #     for b in range(2):
    #         ni = i + di[b]
    #         nj = j + dj[b]
    #         if ni >




    # for j in range(98 ,-1, -1): #세로
    #     if ladder[j][end-1] == 1:


