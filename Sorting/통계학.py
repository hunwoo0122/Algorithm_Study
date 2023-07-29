import sys
input = sys.stdin.readline
n = int(input())
array = []
for i in range(n):
    array.append(int(input()))
    array.sort()

result = sum(array)
aver = result / n
round(aver, 1)
print(aver)
print(array[n // 2])

print(max(array)-min(array))