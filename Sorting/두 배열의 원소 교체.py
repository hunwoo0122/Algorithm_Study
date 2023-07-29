n, k = map(int, input().split()) # n과 k를 입력받기
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if b[i] > a[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))