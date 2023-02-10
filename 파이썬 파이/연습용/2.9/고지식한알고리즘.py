p = "is" #찾을 패턴
t = "This is a book~@" #전체 텍스트
M= len(p) #찾을 패턴의 길이
N = len(t) #전체 텍스트의 길이

# def BruteForce(p, t):
#     i = 0 #t의 인덱스
#     j = 0 #p의 인덱스
#     while j < M and i < N:
#         if t[i] != i < N:
#             i = i -j
#             j = -1
#         i += 1
#         j += 1
#     if j == M: return i - M #검색 성공
#     else: return -1 #검색 실패

###
def bf2(p,t,N,M):
    cnt = 0
    for i in range(N-M+1):
        for j in range(M):
            if t[i+j] != p[j]:
        else:
            cnt += 1
    return cnt
print(bf2(p, t, N, M))