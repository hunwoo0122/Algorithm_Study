n = int(input())

stack = []
for _ in range(n):
    a = int(input())
    if a == 0:
        if len(stack) > 0:
            stack.pop()
    else:
        stack.append(a)

if len(stack) == 0:
    print(0)
else:
    print(sum(stack))
