import sys
input = sys.stdin.readline

t = int(input())
for i in range(1, t + 1):
    a, b, c = map(int, input().split())
    box = []
    cnt = 0
    if b < 2 and c < 3:
        print("#{}".format(i), -1, end=" ")
    else:
        while b >= c:
            b -= 1
            cnt += 1
        while a >= b:
            a -= 1
            cnt += 1
    if a == 0 or b==0 or c==0:
        print("#{}".format(i), -1, end=" ")
    else:
        print("#{}".format(i), cnt, end=" ")
    print()