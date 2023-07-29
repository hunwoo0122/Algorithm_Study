n = int(input())
card = set(map(int, input().split()))
m = int(input())
card_answer = list(map(int, input().split()))
for i in card_answer:
    if i in card:
        print(1, end=' ')
    else:
        print(0, end=' ')
