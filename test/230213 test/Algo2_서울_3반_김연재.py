
T = int(input())
for t in range(1, T+1):
    n = int(input())  # 두더지 몇 번 나오는지
    r, c = map(int, input().split())  # 시작 위치 (계속 변경될 위치)
    score = 0  # 점수를 기록할 변수
    for _ in range(n):
        A, B, k = map(int, input().split())  # 두더지의 좌표와 시간
        while k > 0:  # 초가 남아있을 때까지만 움직인다.
            if B < c:  # 가로로 먼저 움직인다.
                c -= 1  # 위치 변경과 동시에 1초 차감
                k -= 1
                if (A, B) == (r, c):  # 좌표가 같을 경우
                    score += 1  # 1점 획득. 즉시 반복문을 빠져나온다
                    break
                continue  # 가로 조건에서는 동시에 세로에 걸리지 않도록 컨티뉴 사용
            elif B > c:
                c += 1
                k -= 1
                if (A, B) == (r, c):
                    score += 1
                    break
                continue
            if A < r:  # 가로를 충족해서 내려올 경우 세로 조건
                r -= 1
                k -= 1
                if (A, B) == (r, c):
                    score += 1
                    break
            elif A > r:
                r += 1
                k -= 1
                if (A, B) == (r, c):
                    score += 1
                    break
    print(f'#{t} {score}')




