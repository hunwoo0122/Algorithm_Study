array = []
sum = 0
for _ in range(5):
    a = int(input())
    array.append(a)

for i in range(len(array)):
    sum += array[i]
print(int(sum/5))
b = sorted(array)
print(b[2])