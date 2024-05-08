import sys
input = sys.stdin.readline

t = int(input())

def adjacent(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x-i:
            return False
    return True

def dfs(x):
    global result
    if x == n:
        result += 1
    else:
        for i in range(n):
            row[x] = i
            if adjacent(x):
                dfs(x+1)

for i in range(1, t+1):
    n = int(input())
    result = 0
    row = [0] * n
    dfs(0)
    print("#{}".format(i), result, end=" ")
    print()