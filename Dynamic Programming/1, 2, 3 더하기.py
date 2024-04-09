import sys
input = sys.stdin.readline

t = int(input())
array = [0, 1, 2, 4]

def fib(n):
    if n >= 4:
        for i in range(len(array), n+1):
            array.append(array[i-1] + array[i-2] + array[i-3])
    print(array[n])

for _ in range(t):
    n = int(input())
    fib(n)