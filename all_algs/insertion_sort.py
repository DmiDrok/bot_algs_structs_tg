def insertion_sort(a):
    for i in range(1, len(a)):
        pos = i
        while pos > 0 and a[pos-1] > a[pos]:
            a[pos-1], a[pos] = a[pos], a[pos-1]
            pos -= 1

    return a

arr = [100, 15, 20, -3, 9, 52]
res = insertion_sort(arr)
print(res)