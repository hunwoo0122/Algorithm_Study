import sys
n = int(sys.stdin.readline())
array = []
for _ in range(n):
    a = sys.stdin.readline().rstrip()
    array.append(a)
set_array = list(set(array))
sort_array = []
for i in set_array:
    sort_array.append([len(i), i])
sort_array.sort()
for length,char in sort_array:
    print(char)