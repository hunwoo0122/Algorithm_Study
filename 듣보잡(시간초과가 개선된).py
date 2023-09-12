import sys

a, b = map(int, sys.stdin.readline().split())

not_hear = set()
not_see = set()

for _ in range(a):
    n = sys.stdin.readline().strip()
    not_hear.add(n)

for _ in range(b):
    m = sys.stdin.readline().strip()
    not_see.add(m)

# 공통된 값 찾기
common_values = not_hear.intersection(not_see)

common_values = sorted(common_values)

print(len(common_values))
for value in common_values:
    print(value)
