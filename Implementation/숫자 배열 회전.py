import sys
input = sys.stdin.readline

t = int(input())

for i in range(1, t+1):
    n = int(input())
    array = []
    array_90 = []
    array_180 = []
    array_270 = []
    cnt = 0
    for _ in range(n):
        array.append(list(map(int, input().split())))
    for j in range(n):
        temp = []
        for k in range(n-1, -1, -1):
            temp.append(array[k][j])
        array_90.append(temp)

    for j in range(n-1, -1, -1):
        temp = []
        for k in range(n-1, -1, -1):
            temp.append(array[j][k])
        array_180.append(temp)

    for j in range(n-1, -1, -1):
        temp = []
        for k in range(n):
            temp.append(array[k][j])
        array_270.append(temp)
    print("#{}".format(i))
    for j in range(n):
        for k in range(n):
            print(array_90[j][k], end='')
        print(end=" ")
        for m in range(n):
            print(array_180[j][m], end='')
        print(end=" ")
        for a in range(n):
            print(array_270[j][a], end='')
        print()

