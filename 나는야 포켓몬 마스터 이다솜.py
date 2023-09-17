import sys

a, b = map(int, sys.stdin.readline().split())

directory = []
for _ in range(a):
    monster = sys.stdin.readline().strip()
    directory.append(monster)

for _ in range(b):
    query = sys.stdin.readline().strip()
    if query.isdigit():
        index = int(query) - 1
        print(directory[index])
    else:
        index = directory.index(query)
        print(index + 1)

