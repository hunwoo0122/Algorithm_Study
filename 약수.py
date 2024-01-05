n = int(input())
array = list(map(int, input().split()))

max_abr=max(array)
min_abr=min(array)

print(max_abr * min_abr)