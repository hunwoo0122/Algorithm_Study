import sys

# generate a list of prime numbers up to 10,000 using the Sieve of Eratosthenes
limit = 10000
sieve = [True] * limit
sieve[0] = sieve[1] = False
for i in range(2, int(limit ** 0.5) + 1):
    if sieve[i]:
        for j in range(i * i, limit, i):
            sieve[j] = False
primes = [i for i in range(2, limit) if sieve[i]]

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    partition = []
    for i in primes:
        if i > n // 2:
            break
        if n - i in primes:
            partition.append([i, n - i])

    # find the partition with the smallest difference
    min_diff = abs(partition[0][0] - partition[0][1])
    min_pair = partition[0]
    for pair in partition:
        diff = abs(pair[0] - pair[1])
        if diff < min_diff:
            min_diff = diff
            min_pair = pair

    print(*min_pair)