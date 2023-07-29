import itertools
import sys
n = int(sys.readline())
x = []
y = []

if n == 1:
    print(0)
else:
    for i in range(n):
        marble = list(map(int, input().split()))
        x.append(marble[0])
        y.append(marble[1])

max_length = 0
max_height = 0

for p1, p2 in itertools.combinations(range(n), 2):
    length = abs(x[p1] - x[p2])
    height = abs(y[p1] - y[p2])
    max_length = max(max_length, length)
    max_height = max(max_height, height)

print(max_length * max_height)
