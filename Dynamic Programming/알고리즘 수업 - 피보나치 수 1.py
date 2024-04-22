import sys
input = sys.stdin.readline

n = int(input())

f1, f2 = 0, 0
def fib(n):
    a, b = 1, 1
    for i in range(3, n+1):
        a, b = b, a + b
    return b

def fibonacci(b):
    return b-2
print(fib(n), fibonacci(n))