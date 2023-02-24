import sys

sys.stdin = open("input.txt", "r", encoding='UTF-8')

'''
리스트를 방 번호가 아니라 복도를 중심으로 만들어야 한다.
(방번호 -1) // 2: 복도번호
[1] 시작복도 번호 ~ 끝 복도 번호: 누적 cnt 표시
[2] 최대값 찾기
cnt = [0] * 200
for _ (N)
    for j ((s-1)//2, (e-1)//2 + 1)
        cnt[j] += 1
        
방 번호는 홀수나 짝수나 전부 (번호-1)//2를 하면 구해진다.
'''

T = int(input())
for t in range(1, T+1):
    n = int(input())
    cnts = [0] * 200  # 단위 시간을 카운트
    for _ in range(n):
        s, e = map(int, input().split())  # s: 현재 방, e: 돌아갈 방
        if s > e:  # 돌아갈 방보다 현재 있는 방의 번호가 더 클 수도 있기 때문
            s, e = e, s
        for i in range((s-1)//2, (e-1)//2+1):  # 해당하는 복도의 범위만큼 cnts에 +1씩
            cnts[i] += 1

    print(f'#{t} {max(cnts)}')
