n = int(input())
array = []
array_cnt = []
cnt = 0
for _ in range(n):
    a, b = input().split()
    a = int(a)
    cnt += 1
    array_cnt.append(cnt)
    array.append([a, b])
array.sort()
for age, name in array:
    print(age, name)

