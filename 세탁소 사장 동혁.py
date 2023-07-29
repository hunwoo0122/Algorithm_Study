n = int(input())
for i in range(n):
    change = int(input())
    pay = [25, 10, 5, 1]
    number = [0, 0, 0, 0]
    for c in range(len(pay)):
        number[c] += change // pay[c]
        change %= pay[c]
    print(*number)