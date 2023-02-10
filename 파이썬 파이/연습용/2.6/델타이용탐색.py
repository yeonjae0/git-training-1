# arr[0...N-1][0...N-1] #N * N 배열
# di[] <- [0, 0, -1, 1] #상하좌우
# dj <- [-1, 1, 0, 0]
# for i : 0 -> N-1
#     for j : 0 -> N-1
#         for k in range(4):
#             ni <- i + di[k]
#             nj <- j + dj{k}
#             if 0 <= ni < N and 0 <= nj < N #유효한 인덱스면
#                 test(arr[ni][nj])

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N= 3
for i in range(N):
    for j in range(N):
        for k in range(4):
            ni, nj = i+di[k], j + dj[k]
            #print(i, j, ni, nj)
            if 0<=ni<N and 0<=nj<N:
                print(i, j, ni, nj)