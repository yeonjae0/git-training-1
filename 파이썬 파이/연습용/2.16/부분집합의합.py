# 부분집합의 합
def f(i,k):
    if i ==k:
        s = 0  # 하나의 부분집합 완성
        for j in range(k):
            if bit[j]:
                s += A[j]  # 부분집합의 합
                print(A[j], end= ' ')

        #print(bit)
    else:
        bit[i] = 1
        f(i+1, k)
        bit[i] = 0
        f(i+1, k)

A = [1, 2, 3]
N = len(A)
bit = [0]*N
f(0, N)
