def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    global cnt, res
    i = p
    j = q + 1
    tmp = []
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    while i <= q:           # 남은 요소들 추가
        tmp.append(A[i])
        i += 1
    while j <= r:           # 남은 요소들 추가
        tmp.append(A[j])
        j += 1
    i = p
    t = 0
    while i <= r:
        A[i] = tmp[t]
        cnt += 1
        if cnt == m:
            res = A[i]
            break
        i += 1
        t += 1

# 예제로 리스트를 정의하고 테스트합니다.
n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
res = -1
merge_sort(a, 0, len(a) - 1)
print(res)