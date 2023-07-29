n = int(input())
array = []
array2 = []
array3 = []
if n == 1:
    for i in range(n):
        a, b = map(int, input().split())
    print(0)
else:
    for i in range(n):
        marble = list(map(int, input().split()))
        array3.append(marble)
    for i in range(n):
        for j in range(i+1, n):
            length = array3[i][0] - array3[j][0]
            array.append(abs(length))
            height = array3[i][1] - array3[j][1]
            array2.append(abs(height))
    print(max(array)*max(array2))

