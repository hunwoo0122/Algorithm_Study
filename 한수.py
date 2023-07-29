n = int(input())
count = 0
for i in range(1, n+1):
    jalitsu = list(map(int, str(i)))
    if i<100:
        count += 1
    elif jalitsu[0] - jalitsu[1] == jalitsu[1] - jalitsu[2]:
        count +=1
print(count)


