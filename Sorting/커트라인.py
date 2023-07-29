n, k = map(int, input().split())
student = list(map(int, input().split()))
cut = sorted(student, reverse=True)
print(cut[k-1])