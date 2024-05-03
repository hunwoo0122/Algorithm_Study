import sys
sys.stdin = open("../Implementation/input.txt")

t = int(input())

for i in range(1, t+1):
    n = int(input())
    pascal = [[1] * (k+1) for k in range(n)]
    print("#{}".format(i))
    for j in range(n):
        for q in range(j+1):
            if q == 0 or q == j:
                pascal[j][q] = 1
            else:
                pascal[j][q] = pascal[j-1][q-1] + pascal[j-1][q]
        print(*pascal[j])

