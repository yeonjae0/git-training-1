
def collatz(num):
    cnt = 0
    while num != 1: #1이 아닐 때 무한루프
        if num == 1:
            break
        elif num % 2 == 0:
            cnt += 1
            num = num / 2
            if cnt >= 500: #카운트가 500이 넘어도 돌면 그냥 -1 반환
                return print(-1)
        elif num % 2 == 1:
            cnt += 1
            num = num * 3 + 1
            if cnt >= 500:
                return print(-1)
    return print(cnt)

        
collatz(6) #=> 8
collatz(16) #=> 4
collatz(27) #=> 111
collatz(626331) #=> -1