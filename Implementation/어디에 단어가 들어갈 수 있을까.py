import sys
input = sys.stdin.readline
t = int(input())

for i in range(1, t + 1):
    n, k = map(int, input().split())
    array = []
    for _ in range(n):
        array.append(list(map(int, input().split())))
    word = 0
    for q in range(n):
        cnt = 0
        for j in range(n):
            if array[q][j] == 1:
                cnt += 1
            if array[q][j] == 0 or j == n-1:
                if cnt == k:
                    word += 1
                cnt = 0
        for m in range(n):
            if array[m][q] == 1:
                cnt += 1
            if array[m][q] == 0 or m == n-1:
                if cnt == k:
                    word += 1
                cnt = 0
    print("#{}".format(i),word, end=" ")
    print()