import sys
sys.stdin = open("../input.txt")

t = int(input())

for i in range(1, t + 1):
    n, m = map(int, input().split())
    array = []
    fly = []
    max_value = 0
    for _ in range(n):
        array.append(list(map(int, input().split())))
    for j in range(n-m+1):
        for k in range(n-m+1):
            cnt = 0
            for q in range(j, j+m):
                for w in range(k, k+m):
                    cnt += array[q][w]
                    if max_value < cnt:
                        max_value = cnt
    print("#{}".format(i), max_value, end=" ")
    print()
