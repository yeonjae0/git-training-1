def f(i,k):
    if i == k:
        print(p)
    else:
        for j in range(i, k):  # 중복을 피하기 위해서는 왼쪽으로는 교환 x
            p[i], p[j] = p[j], p[i]
            f(i+k, k)
            p[i], p[j] = p[j], p[i]

p = [1,2,3]
N = len(p)
f(0, N)

