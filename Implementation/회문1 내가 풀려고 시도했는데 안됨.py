import sys
input = sys.stdin.readline

for i in range(1, 11):
    n = int(input())
    array = []
    for j in range(8):
        array.append(list(input().strip()))
    line = [[array[j][i] for j in range(8)] for i in range(8)]
    cnt = 0
    for j in range(8):
        for k in range(8 - n + 1):
            if array[j][k:k+n] == array[j][k:k+n][::-1]:
                cnt += 1
    for j in range(8):
        for k in range(8 - n + 1):
            if line[j][k:k+n] == line[j][k:k+n][::-1]:
                cnt += 1

    print("#{}".format(i), cnt, end=" ")
    print()