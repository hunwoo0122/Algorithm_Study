paper = [[0 for i in range(100)] for j in range(100)]

n = int(input())
for i in range(n):
    a, b = map(int, input().split())

    for j in range(a,a+10):
        for k in range(b,b+10):
            paper[k][j] = 1
result = 0
for i in paper:
    result += i.count(1)
print(result)