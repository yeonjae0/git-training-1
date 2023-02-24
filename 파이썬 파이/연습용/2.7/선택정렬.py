def selectionsort(a,n):
    for i in range(n-1):
        minidx = i
        for j in range(i+1, n):
            if a[minidx] > a[j]:
                minidx = j
        a[i], a[minidx] = a[minidx], a[i]