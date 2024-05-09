import sys
input = sys.stdin.readline

t = int(input())

for i in range(1, t + 1):
    n = int(input())       # n은 9
    farm = []
    for _ in range(n):
        farm.append(list(map(int, input().strip())))

    result = 0
    temp = []
    x = n // 2         # x는 4
    for j in range(x): # j는 0 1 2 3 4
        s = x - j
        e = x + j
        a = n - 1 - j
        for m in range(s, e + 1):
            result += farm[j][m]
            result += farm[a][m]

    for k in range(n):
        result += farm[x][k]

    print("#{}".format(i), result, end=" ")
    print()