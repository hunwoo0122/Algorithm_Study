n = int(input())
array = []
array2 = []
for _ in range(n):
    a, b = map(int, input().split())
    array.append(a)
    array2.append(b)

x= max(array)-min(array)
y= max(array2)-min(array2)

print(x*y)