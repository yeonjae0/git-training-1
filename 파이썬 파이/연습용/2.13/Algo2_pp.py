import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')

T = int(input())
for t in range(1, T+1):
    n = int(input())  # 두더지 몇 번 나오는지
    r, c = map(int, input().split())  # 시작 위치 (계속 변경될 위치)
    score = 0  # 점수를 기록할 변수
    for _ in range(n):
        A, B, k = map(int, input().split())  # 두더지의 좌표와 시간
        while k > -1:  # 초가 남아있을 때까지만 움직인다.
            if (A, B) == (r, c):
                score += 1
                break
            else:
                if B < c:  # 가로로 먼저 움직인다.
                    c -= 1
                    k -= 1
                    continue
                elif B > c:
                    c += 1
                    k -= 1
                    continue
                if A < r:
                    r -= 1
                    k -= 1
                elif A > r:
                    r += 1
                    k -= 1
    print(f'#{t} {score}')

# 여기서는 왜 첫 테케의 값이 이상하게 나올까
#여기서 score를 저장하기 위해 한 번 더 와일문을 돌 수 있게 시간 조건을 설정하니까
#두더지를 처음에 못잡을 때 위치가 한 번 더 갈 수 있는 위험이 있다.