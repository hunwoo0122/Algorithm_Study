array = list(map(int, input().split()))
array.sort()
result = array[0] + array[1]
if result <= array[2]:
    print(array[0] + array[1] + result - 1)
else:
    print(sum(array))