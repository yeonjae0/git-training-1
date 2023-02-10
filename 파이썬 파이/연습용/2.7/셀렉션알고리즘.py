#일반적인 셀렉션 알고리즘
def select(arr, k):
    for i in range(0, k):
        minidx = i
        for j in range(i+1, len(arr)):
            if arr[minidx] > arr[j]:
                minidx = j
        arr[i], arr[minidx] = arr[minidx], arr[i]
    return arr[k-1]