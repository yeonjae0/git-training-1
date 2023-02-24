#Gravity
T = int(input())
for a in range(T):
    N = int(input())
    box_list = list(map(int, input().split()))
    ans_list = []
    for i in range(len(box_list)): #수열의 길이만큼 반복문
        cnt = N-1-i # 기본적으로 떨어질 수 있는 최대치
        for j in range(i+1, N): #상자의 맨 끝값만 판별한다고 생각
            if box_list[i] <= box_list[j]: #해당 숫자보다 작으면 전부 낙차 1씩 차감
                cnt -= 1
            #print (cnt)
        ans_list.append(cnt) #최대로 떨어질 수 있는 숫자들의 리스트
    ans = 0
    for x in range(len(ans_list)): # 위의 리스트에서 최대값 구하기
        if x == 0:
            ans = ans_list[0]
        elif ans_list[x] > ans:
            ans = ans_list[x]
    print(f'#{a+1} {ans}')



