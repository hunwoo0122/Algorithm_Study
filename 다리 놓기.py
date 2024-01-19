import sys
input = sys.stdin.readline
t = int(input())

def factorial(a):
    r = 1
    for i in range(1, a+1):
        r = r * i
    return r

for _ in range(t):
    n, m = map(int, input().split())
    print(factorial(m)//(factorial(m - n) * factorial(n)))
