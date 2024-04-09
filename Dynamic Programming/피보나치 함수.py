import sys
input = sys.stdin.readline

zero = [1, 0, 1]  # zero[idx]는 fibonacci(0)이 fibonacci(idx)일때 호출된 횟수
one = [0, 1, 1]   # one[idx]는 fibonacci(1)이 fibonacci(idx)일때 호출된 횟수

def fibonacci(n):
    length = len(zero)
    if n >= length:
        for i in range(length, n + 1):
            zero.append(one[i-1])
            one.append(zero[i-1] + one[i-1])
    print(zero[n], one[n])

# 재귀로 구현하면 시간초과 남

t = int(input())
for _ in range(t):
    n = int(input())
    fibonacci(n)