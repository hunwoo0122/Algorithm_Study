n = int(input())
data = list(map(int, input().split()))
a = max(data)
b = []
for score in data:
    score = score / a *100
    b.append(score)
average = sum(b[0:])/n
print(average)