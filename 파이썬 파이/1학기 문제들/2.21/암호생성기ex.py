import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    data = list(map(int, input().split()))  # 받은 input 자체를 q로 활용
    # 현재 싸이클에서 감소시켜줘야하는 값
    cnt = 1

    while data[-1] > 0:
        if cnt > 5:
            cnt = 1

        # 첫번째 위치한 숫자를 감소시킨 뒤 맨 뒤로 보내기
        data.append(data.pop(0) - cnt)
        cnt += 1
    # 데이터의 마지막 값은 0으로 고정
    data[-1] = 0