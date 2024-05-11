import sys
input = sys.stdin.readline


t = int(input())
for i in range(1, t + 1):
    mem = list(input().strip())
    length = len(mem)
    init = [0] * length
    cnt = 0
    for j in range(length):
        if init[j] != int(mem[j]):
            for k in range(j, length):
                init[k] = int(mem[j])
            cnt += 1
        else:
            continue
    print("#{}".format(i), cnt, end=" ")
    print()