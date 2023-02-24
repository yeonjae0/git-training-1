T = int(input())

for a in range(T):
    num = int(input())
    c = [0] * 10 # 0~9

    for _ in range(6):
        c[num % 10] += 1
    #456789의 9 -> c[9] +=1 
        #8-> c[8]+= 1
        num //= 10 #c에 카운팅 정렬
        print(c)

    i = 0
    tri = run = 0
    while i < 10:
        if c[i] >= 3: #카운팅한게 3보다 큰게 있으면 tri
            c[i] -= 3 #다시 초기화
            tri += 1
            continue
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            run += 1
            continue
        i += 1

    if run + tri == 2: print(f'#{a} 1')
    else: print(f'#{a+1} 0')