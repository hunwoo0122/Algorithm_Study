import sys
sys.stdin = open("../input.txt")
t = int(input())

for i in range(1, t + 1):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    array = []
    result = 0
    if n < m: # len(B)가 3, len(A)가 5인 경우
        for k in range(m-n+1):
            cnt = 0
            for j in range(k, k + n):
                result += A[cnt] * B[j]
                cnt += 1
            array.append(result)
            result = 0
    elif n > m:
        for q in range(n-m+1):
            cnt = 0
            for c in range(q, q + m):
                result += A[c] * B[cnt]
                cnt += 1
            array.append(result)
            result = 0
    else:
        for d in range(n):
            result += A[d] * B[d]
        array.append(result)
    print("#{}".format(i), max(array), end=" ")
    print()