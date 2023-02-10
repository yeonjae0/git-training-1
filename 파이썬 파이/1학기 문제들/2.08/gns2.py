#gns 카운팅으로
import sys
sys.stdin = open("input.txt", "r")

str_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

t = int(input())
for a in range(1, t+1):
    cnt = [0] * 10 #여기에 숫자만큼 더해줄 생각 / 초기화
    #print(cnt)
    ht, num = input().split()
    case = list(input().split()) #이게 문자열들 리스트
    for i in range(10):
        for word in case:
            if word == str_list[i]: #문자열의 요소가 해당 리스트의 값과 같다면
                cnt[i] += 1 #0 리스트의 인덱스 번호에 +1
    print(cnt)
    #여긴 프린트 구역
    print(ht)
    for j in range(10):
        for k in range(cnt[j]):
            print(str_list[j], end=' ')
    print()