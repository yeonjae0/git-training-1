# a = [ 1, 2, 3, 4, 3, 2 , 2]
# cnt = [0] * 5 # 5 == max(a)+1
# for i in a:
#     cnt[i] += 1
# print(cnt)

#카운팅소트
# def Counting_sort(a, b, k)
#     A = [] #-- 입력 배열(0 to k) Data
#     B = [] #-- 정렬된 배열 Temp
#     C = [] #-- 카운트 배열 Counts
#     k = max(A) #k는 주어질 조건 / 입력 배열 0<k<100 등
    
#     C = [0] * (K+1)

#     for i in range(0, len(A)): #for 문이 도는데 n만큼의 시간
#         C[A[i]] += 1

#     for i in range (1, len(C)): #for문이 도는데 k만큼의 시간
#         C[i] += C[i-1]

#     for i in range (len(B)-1, -1, -1):
#         C[A[i]] -= 1
#         B[C[A[i]]] = A[i]

#baby gin
# num = 456789 #baby gin 확인할 6자리 수
# c = [0] * 12 #6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트

# for i in range(6):
#     c[num % 10] += 1
#     #456789의 9 -> c[9] +=1 
#     #8-> c[8]+= 1
#     num //= 10
