import sys
input = sys.stdin.readline

cnt = 0
array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
check = [0] * 10
n = input().strip()
for i in n:
    check[array.index(i)] += 1
cnt_6 = check[6]
cnt_9 = check[9]
sum_69 = cnt_6 + cnt_9
if sum_69 % 2 == 0:
    sum_69 = sum_69//2
else:
    sum_69 = (sum_69+1)//2
max_cnt0 = 0
max_cnt1 = 0
for j in range(0, 6):
    max_cnt0 = max(check[j], max_cnt0)
for k in range(7, 9):
    max_cnt1 = max(check[k], max_cnt1)
print(max(max_cnt0,max_cnt1,sum_69))