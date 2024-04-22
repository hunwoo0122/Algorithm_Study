import sys
input = sys.stdin.readline

T = int(input())

zero = [1, 0, 1]
one = [0, 1, 1]
def fib(n):
    length = len(zero)
    if length >= 3:
        for i in range(length, n + 1):
            zero.append(one[i-1])
            one.append(zero[i-1] + one[i-1])
    return zero[n], one[n]


for _ in range(T):
    n = int(input())
    print(*fib(n))
