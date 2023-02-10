a= [55, 7, 78, 12, 42]
N= 5
def bubblesort(a ,N):
    for i in range(N-1, 0, -1): #각 구간의 끝
        #print(i)
        for j in range(0, i): #비교할 왼쪽 원소
            
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j] #큰 원소 오른쪽으로
                print(f'#{a[j]}')
    return print(a)
bubblesort(a,N)