def calc(idx, cnt):
    global result
    # "가지치기"
    # 애초에 내가 지금 가지고온 cnt 값이
    # 현재 최솟값보다 크면
    # 더 이상 조사할 필요가 없다.
    if cnt >= result:
        return

    # 모든 행을 다 조사 했을때,
    if idx == n:
        # 최솟값 구하기
        if result > cnt:
            result = cnt
        return

    # 조사를 시작
    # idx -> 행, i -> 열
    for i in range(n):
        if selected[i] == 0:
            # 써보자
            selected[i] = 1
            # 쓰기로 한 상태 -> cnt에 해당위치 값 더하고
            # 다음 행 조사로 넘어가기
            calc(idx+1, cnt + data[idx][i])
            # 썼었던거 제자리로 돌려주기 (초기화)
            selected[i] = 0


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]

    # 최종 결괏값
    result = 0
    for i in range(n):
        result += sum(data[i])

    # 선택 여부 확인용 리스트
    selected = [0] * n

    # 현재 조사 위치, 총합
    calc(0, 0)
    print(f'#{tc} {result}')
