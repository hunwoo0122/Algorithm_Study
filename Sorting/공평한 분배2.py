import sys
input = sys.stdin.readline

t = int(input())
for i in range(1, t + 1):
    n, k = map(int, input().split())
    pocket = list(map(int, input().split()))
    pocket.sort()
    min_differ = float('inf')
    for j in range(n-k+1):
        differ = pocket[j + k - 1] - pocket[j]
        if differ <= min_differ:
            min_differ = differ

    print("#{}".format(i), min_differ, end=" ")
    print()