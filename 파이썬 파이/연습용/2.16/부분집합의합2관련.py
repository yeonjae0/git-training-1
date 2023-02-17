def f(i, k, s, t):
    """
    i: 원소 (A리스트의 인덱스를 옮기기 위한 값)
    k: 집합의 크기
    s: i-1까지 고려된 합
    t: 목표
    """
    global cnt
    if s > t:  # 고려한 원소의 합이 찾는 합 보다 큰 경우 함수 종료
        return  # 함수 호출을 적게 하기 위함

    if i == k:  # 끝까지 갔을 때
        if s == t:
            cnt += 1
        return
    else:
        f(i + 1, k, s + A[i], t)  # A[i] 포함
        f(i + 1, k, s, t)  # A[i] 미포함


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(A)
key = 10
cnt = 0
bit = [0] * N
f(0, N, 0, key)
print(cnt)  # 합이 key인 부분집합의 수