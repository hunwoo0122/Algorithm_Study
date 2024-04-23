import sys
input = sys.stdin.readline

n = int(input())

array = [0, 1]

for i in range(2, abs(n)+1):
    array.append((array[i-1]+array[i-2]) % 1000000000)
if n < 0 and n % 2 == 0:
    print(-1)
elif n == 0:
    print(0)
else:
    print(1)
print(array[abs(n)])
