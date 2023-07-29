n = int(input())

count = 1
edge = 6
start = 1
while True:
    start += edge
    if n == 1:
        print(1)
        break
    count += 1
    if n <= start:
        print(count)
        break
    edge += 6