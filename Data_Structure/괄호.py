n = int(input())
for _ in range(n):
    stack = []
    a = input()
    for j in a:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else: # ()) 인 경우
                print('NO')
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")
