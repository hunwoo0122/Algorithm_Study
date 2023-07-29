m = int(input())
n = int(input())

array = []
for i in range(m, n + 1):
    error = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                error += 1
        if error == 0:
            array.append(i)
if not array:
    print(-1)
else:
    print(sum(array))
    print(min(array))
