import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n+1):
    i = str(i)
    a = i.count('3') + i.count('6') + i.count('9')
    if a:
        print("-"*a, end=" ")
    else:
        print(i, end=" ")
