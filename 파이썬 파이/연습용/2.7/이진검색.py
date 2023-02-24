#이진 검색 알고리즘
def binarysearch(a, n, key):
    start = 0
    end = n-1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key: #검색성공
            return True
        elif a[middle] > key:
            end = middle -1
        else:
            start = middle + 1
    return False #검색실패

# 재귀함수 이용 (그런데 반복 구조가 더 빠름)
def binarysearch2(a, low, high, key):
    if low > high: #검색실패
        return False
    else:
        middle = (low + high) // 2
        if key == a[middle]: #검색성공
            return True
        elif key < a[middle]:
            return binarysearch2(a, low, middle-1, key)
        elif a[middle] < key:
            return binarysearch2(a, middle+1, high, key)