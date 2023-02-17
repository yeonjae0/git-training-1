def f(i,k,s,t):  #i 원소, k 집합의 크기, s i-1까지 고려된 합, t 찾고자 하는 합(목표)
    global cnt
    if i == k:
        if s == t:
            # for j in range(k):
            #     if bit[j]:
            #         print(A[j], end= ' ')
            cnt += 1
            #ans.append(s)
        return
    else:
        #s += A[i]
        f(i+1, k, s+A[i], t)  #A[i] 포함
        f(i + 1, k, s, t)  # A[i] 미포함

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(A)
key = 10
cnt = 0
bit = [0]*N
#ans = []

f(0, N, 0, key)
print(cnt)  # 합이 key인 부분집합의 수
#print(ans)