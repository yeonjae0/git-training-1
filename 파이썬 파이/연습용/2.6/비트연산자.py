arr = [3,6,7,1,5,4]
n = len(arr)     #n: 원소의 개수
for i in range(1<<n):    #1<<n: 부분집합의 개수
    for j in range(n):    #원소의 수만큼 비트를 비교
        if i & (1<<j):     #i의 j번 비트가 1인 경우
            print(arr[j], end = ', ') #j번째 원소 출력
    print() #이 프린트는 행 구분 (for문 한 번이 한 줄)
#print() #이건 굳이?