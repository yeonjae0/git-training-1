#전기버스
T = int(input())
for a in range(T):
    k, n, m = map(int, input().split())
    m_list = list(map(int, input().split()))

    position = 0 #내가 있는 위치/ 계속 업뎃 예정
    cnt = 0 #답이 될 충전 횟수
    
    while position + k < n: #내 위치와 거리가 n보다 작을 때까지
        for i in range(k, 0, -1):
            if position + i in m_list: # 움직인 거리에 충전소가 있는지 (없으면k-1씩)
                position += i #i만큼 움직이기
                cnt += 1
                break #for문에서 벗어나기
       
        
        else:
            cnt = 0
            break
    print(f'#{a+1} {cnt}')


