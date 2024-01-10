import sys
input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    a = input().rstrip()
    if len(a) > 2:    # a[0]이 1일 경우
        stack.append(int(a[2:]))
    elif a == '2':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif a == '3':
        print(len(stack))
    elif a == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif a == '5':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])