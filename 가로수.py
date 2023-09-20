import math
n = int(input())
array = []
array2 = []
array3 = []
cnt = 0

for i in range(n):
    array.append(int(input()))

for i in range(1, n):  # 수정된 부분: i의 범위를 1부터 n-1까지로 변경
    yaksu = array[i] - array[i - 1]  # 수정된 부분: i번째와 (i-1)번째 값의 차이를 계산
    array2.append(yaksu)
gcd_result = array2[0]
for j in range(1, len(array2)):
    gcd_result = math.gcd(gcd_result, array2[j])
for k in range(1, len(array)):
    if array[k] - array[k-1] != gcd_result:
        cnt += (array[k]-array[k-1])//gcd_result-1
print(cnt)
