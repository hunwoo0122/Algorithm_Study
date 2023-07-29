a, b, v = map(int, input().split())

arrive = v-a
distance = a - b
days = 0
if arrive < distance:
    result = v // distance + 1
else:
    result = arrive // distance + 1
print(result)