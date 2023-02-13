
T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    ans = set()  # 중복되는 좌표를 피하기 위해서 집합으로 설정
    for _ in range(m):
        x, y, w, h = map(int, input().split())  # 행, 열, 너비, 높이
        for i in range(y, y + w):  # 가로
            for j in range(x, x + h):  # 세로
                if (i < n) and (j < n):  # 범위
                    ans.add((i, j))  #튜플로 만들어서 좌표 넣어주기
    print(f'#{t} {len(ans)}')


