#1954 달팽이숫자
import sys
sys.stdin = open("input.txt", "r")

t = int(input())
di = [0, 1, 0, -1] #오른쪽,아래,왼쪽,위
dj = [1, 0, -1, 0]


for a in range(1, t+1):
    graph = []
    n = int(input())
    for _ in range(n):
        graph.append([0]*n) #각 칸에 우선 0 부여
    # print(f'0이 채워진 그래프 {graph}')

    #[i][j] i와 j의 값은 그냥 쭉 0 고정

    ni = 0
    nj =0
    graph[ni][nj] = 1
    num = 1 #0에 더해줄 숫자

    while True:
        if num < n: #초반 한 줄의  k값을 지정해주기 위한 조건문
            k = 0
        ni += di[k]
        nj += dj[k]

        if (0 <= ni < n) and (0 <= nj < n) and (graph[ni][nj] == 0):
            # print(f'첫번째 확인지점 ni {ni}')
            # print(f'첫번째 확인지점 nj {nj}')
            num += 1
            graph[ni][nj] += num
            # print(f'첫번째 확인지점 graph {graph}')
            # print(f'첫번째 확인지점 cnt {cnt}')
            # print(f'첫번째 확인지점 num {num}')

            if num >= (n * n):
                # print('끝')
                break
            #print('d')
        else:
            ni -= di[k] #범위에서 벗어나 else로 넘어왔기 때문에 다시
            nj -= dj[k] #위치를 바로 이전으로 초기화 시켜줘야함.
            #k += 1
            k = (k + 1) % 4
            # if k == 4:
            #     # print('k=3 됨')
            #     k = 0
            #continue
#여긴 프린트
        # 여긴 프린트
        print(f'#{a}', end='')
        for z in range(n):
            print()
            for x in range(n):
                print(graph[z][x], end=' ')
        print()
    #print()

    #print(graph)







