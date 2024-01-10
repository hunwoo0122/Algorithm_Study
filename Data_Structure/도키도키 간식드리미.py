import sys
input = sys.stdin.readline
n = int(input())
line = list(map(int, input().split()))
target = 1
tmp = []
while target != n:
    if len(line) != 0 and line[0] == target:
        line.pop(0)
        target += 1
    elif len(tmp) != 0 and tmp[-1] == target:
        tmp.pop()
        target += 1
    else:
        tmp.append(line.pop(0))
        if len(tmp) > 1 and tmp[-1] > tmp[-2]:
            print("Sad")
            sys.exit()
if (len(tmp) == 1 and len(line) == 0 and tmp[-1] == target) or (len(tmp) == 0 and len(line) == 1 and line[-1] == target):
    print("Nice")
else:
    print("Sad")