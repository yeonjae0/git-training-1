
a = [100, 7, 78, 12, 42, 1, 3, 99]
N = 8
def bubble_sort(a, N):
    for j in range(N-1):
        for i in range(N-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                #print (a)
    return a

print(bubble_sort(a, N))