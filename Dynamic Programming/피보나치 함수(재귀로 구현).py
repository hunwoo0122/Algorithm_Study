import sys
input = sys.stdin.readline

T = int(input())
def fib_cnt(n, ct0, ct1):
    if n == 0:
        ct0 += 1
        return 0, ct0, ct1
    elif n == 1:
        ct1 += 1
        return 1, ct0, ct1
    else:
        fib_n_1, ct0, ct1 = fib_cnt(n - 1, ct0, ct1)
        fib_n_2, ct0, ct1 = fib_cnt(n - 2, ct0, ct1)
        return fib_n_1 + fib_n_2, ct0, ct1

for _ in range(T):
    n = int(input())
    fib_result, f0, f1 = fib_cnt(n, 0, 0)
    print(f0, f1)