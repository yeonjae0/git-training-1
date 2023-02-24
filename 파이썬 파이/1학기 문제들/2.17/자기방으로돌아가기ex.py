# 13801 SWEA 자기 방으로 돌아가기
'''
리스트를 방 번호가 아니라 복도를 중심으로 만들어야 한다.
(방번호 -1) // 2: 복도번호
[1] 시작복도 번호 ~ 끝 복도 번호: 누적 cnt 표시
[2] 최대값 찾기
cnt = [0] * 200
for _ (N)
    for j ((s-1)//2, (e-1)//2 + 1)
        cnt[j] += 1
'''
import sys

sys.stdin = open("input.txt", "r", encoding='UTF-8')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cnts = [0] * 200
    for _ in range(N):
        s, e = map(int, input().split())
        if s > e :  # start 지점이 end 지점보다 숫자가 작다는 말은 어디에도 없음.
            s, e = e, s
        for i in range((s-1)//2, (e-1)//2 + 1):
            cnts[i] += 1

    ans = max(cnts)  # !!겹치는 만큼 단위 시간이 걸린다.!!

    print(f'#{test_case} {ans}')

# 명시된 테케 외에 오류가 났을 때는
# 모두 0? 모두 mx? 정렬 x?
# 문제를 꼼꼼하게 읽어야 한다.