import sys
input = sys.stdin.readline

cnt = 0
array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
check = [0] * 10  # 입력한 문자열의 숫자의 개수를 세기 위한 리스트 생성
n = input().strip()
for i in n:
    check[array.index(i)] += 1  # 숫자가 나타난 개수만큼 check 리스트에 기록
cnt_6 = check[6]
cnt_9 = check[9]
sum_69 = cnt_6 + cnt_9 # 6과 9의 개수를 변수에 기록
if sum_69 % 2 == 0:
    sum_69 = sum_69//2
else:
    sum_69 = (sum_69+1)//2
max_cnt0 = 0
max_cnt1 = 0
for j in range(0, 6):               # 0부터 6의 갯수중 최대 갯수를 구하기
    max_cnt0 = max(check[j], max_cnt0)
for k in range(7, 9):    # 7부터 8의 갯수중 최대 갯수를 구하기
    max_cnt1 = max(check[k], max_cnt1)
print(max(max_cnt0,max_cnt1,sum_69)) # 기록돼 있는 수중 최댓값를 구함