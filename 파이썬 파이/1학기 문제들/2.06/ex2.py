import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for a in range(T):
    num = list(map(str, input().split()))
    ans = []
    lst = []

    for i in range(1<<len(num)):
        subset = []
        for j in range(len(num)):
            #subset = []
            if i & (1<<j):
                #print(num[j], end = ' ')
                subset.append(num[j])
                #ans += [num[j]]
        #lst.append(ans)
        print(subset)

#한 줄씩 나오는 부분집합을 줄 별로 리스트로 묶은 뒤에 리스트에 넣어줄 방법...!