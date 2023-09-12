import sys

a, b = map(int, sys.stdin.readline().split())

not_hear = []
not_see = []
cnt = 0
for _ in range(a):
    n = sys.stdin.readline().strip()
    not_hear.append(n)

for _ in range(b):
    m = sys.stdin.readline().strip()
    not_see.append(m)
array = []
for i in not_hear:
    for j in not_see:
        if i == j:
            cnt += 1
            array.append(i)

array = sorted(array)
print(cnt)
for k in array:
    print(k)