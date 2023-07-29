n = int(input())
array2 = []
for i in range(1, n+1):
    array = []
    hab = 0
    for j in str(i):
        array.append(int(j))
    hab += i
    for k in array:
        hab += k
    if hab == n:
        array2.append(i)
if len(array2) == 0:
    print(0)
else:
    print(min(array2))
