n = int(input())
k = 2
b = 1
for i in range(1, 16):
    k = k + b
    b = 2 * b
    if i == n:
        break
print(k**2)