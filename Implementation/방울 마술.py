import sys
input = sys.stdin.readline
# 동전 앞면 -> 왼쪽 컵과 가운데 컵 위치 스왑, 동전 뒷면 -> 오른쪽 컵과 가운데 텁 위치 스왑
t = int(input())
for i in range(1, t + 1):
    s, k = input().strip().split()
    k = int(k)
    if k >= 2:
        if k % 2 == 0:
            if s == '.o.':
                print("#{}".format(i), 1, end=" ")
            elif s == '..o' or s == 'o..':
                print("#{}".format(i), 0, end=" ")
        else:
            if s == '.o.':
                print("#{}".format(i), 0, end=" ")
            else:
                print("#{}".format(i), 1, end=" ")
    elif k == 1:
        if s == 'o..' or s == '..o':
            print("#{}".format(i), 1, end=" ")
        elif s == '.o.':
            print("#{}".format(i), 0, end=" ")
    elif k == 0:
        if s == 'o..':
            print("#{}".format(i), 0, end=" ")
        elif s == '.o.':
            print("#{}".format(i), 1, end=" ")
        elif s == '..o':
            print("#{}".format(i), 2, end=" ")
    print()