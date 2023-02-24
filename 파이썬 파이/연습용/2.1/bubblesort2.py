#가장 큰 값을 출력
# 2
# 5
# 23 4 5 6 64
# 2
# 88 45

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    maxV = arr[0] #첫 원소를 최대로 가정
    for i in range(1,N):   #나머지 원소와 비교
        if maxV < arr[i]:
            maxV = arr[i]
    print(f'#{tc} {maxV}')


