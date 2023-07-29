n, m = map(int, input().split())
card = list(map(int, input().split()))
card_sum = []
for i in range(len(card)-2):
    for j in range(i+1, len(card)-1):
        for k in range(j+1, len(card)):
            card_sum.append(card[i]+card[j]+card[k])

card_set = list(set(card_sum))
array = []
for i in range(len(card_set)):
    if card_set[i] <= m:
        array.append(card_set[i])

print(max(array))