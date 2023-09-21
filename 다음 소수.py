import sys
import math
n = int(sys.stdin.readline())
def is_prime_number(x):
    if x == 0 or x == 1:
        return False
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x))+1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수 아님
    return True


for _ in range(n):
    a = int(sys.stdin.readline())
    while True:
        if is_prime_number(a):
            print(a)
            break
        else:
            a += 1
