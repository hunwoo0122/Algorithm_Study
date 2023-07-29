n = int(input())
array = []

for i in str(n):
    array.append(i)

a = sorted(array, reverse=True)
print(*a, sep='')