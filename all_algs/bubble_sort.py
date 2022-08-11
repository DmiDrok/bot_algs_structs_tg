a = [...]
N = len(a)
for bypass in range(1, N):
    for i in range(N-bypass):
        print(i)
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]