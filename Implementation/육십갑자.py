import sys
input = sys.stdin.readline

t = int(input())
for i in range(1, t + 1):
    n, m = map(int, input().split()) # n은 s의 길이 m은 t의 길이
    s = list(map(str, input().split()))
    t = list(map(str, input().split()))
    q = int(input())
    gabja = []
    command_line = []
    for _ in range(q):
        command = int(input())
        command_line.append(command)
    if n > m:
        for j in command_line:
            gabja.append(s[j % n-1] + t[j % m-1])
    elif n < m:
        for j in command_line:
            gabja.append(s[j % n-1] + t[j % m-1])
    else:
        for j in command_line:
            gabja.append(s[j % n-1] + t[j % m-1])
    print("#{}".format(i), *gabja, end=" ")
    print()