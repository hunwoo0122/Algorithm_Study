a = int(input())
for i in range(a):
    data = list(map(int, input().split()))
    average = sum(data[1:]) / data[0]
    count = 0
    for score in data[1:]:
        if average < score:
            count += 1
    ratio = count / data[0] * 100
    print(f'{ratio:.3f}%')   # print문이 첫 번째 for문에 있어야 줄마다 출력됨
