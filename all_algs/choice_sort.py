def choice_sort(a):
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a


arr = [100, 15, 20, -3, 9, 52]
res = choice_sort(arr)
print(res)