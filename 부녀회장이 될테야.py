t = int(input())

floor = []
for i in range(t):
    k = int(input())
    n = int(input())
    f0 = [x for x in range(1, n+1)]
    for j in range(k):
        for m in range(1, n):
            f0[m] += f0[m - 1]
    print(f0[-1])