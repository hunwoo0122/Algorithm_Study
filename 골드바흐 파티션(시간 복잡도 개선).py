import sys

input = sys.stdin.readline

prime_num = [False, False] + [True] * 999999

for i in range(2, 1000001):
    if prime_num[i]:
        for j in range(i*2, 1000001, i):
            prime_num[j] = False

t = int(input())

for _ in range(t):
    count = 0
    a = int(input())
    for i in range(2, a//2+1):
        if prime_num[i] and prime_num[a-i]:
            count += 1
    print(count)