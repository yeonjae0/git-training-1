#서울시의 버스노선
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for a in range(T):
    N = int(input())
    cnt = [0] * 5001
    p_list = []
    ans = []
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1): #버스가 다니는 노선만큼 +1 씩 인덱스로 cnt에 추가
            cnt[i] += 1
    P = int(input())

    for j in range(P):
        p_list.append(int(input()))
        ans.append(cnt[p_list[j]])
        #print(f'이건 p_list값 {p_list}')
        #print(cnt[p_list[j]], end=' ') #이거로 안되는건 오류...
    print(f"#{a+1}", *ans)



