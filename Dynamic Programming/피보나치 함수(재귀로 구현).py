import sys
input = sys.stdin.readline

T = int(input())
def fibonacci_with_count(n, count_0, count_1):
    if n == 0:
        count_0 += 1
        return 0, count_0, count_1
    elif n == 1:
        count_1 += 1
        return 1, count_0, count_1
    else:
        fib_n_1, count_0, count_1 = fibonacci_with_count(n - 1, count_0, count_1)
        fib_n_2, count_0, count_1 = fibonacci_with_count(n - 2, count_0, count_1)
        return fib_n_1 + fib_n_2, count_0, count_1

for _ in range(T):
    n = int(input())
    fib_result, f0, f1 = fibonacci_with_count(n, 0, 0)
    print(f0, f1)