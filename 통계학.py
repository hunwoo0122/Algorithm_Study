import sys
import math
input = sys.stdin.readline
n = int(input())
array = []
max_freq = 0
mode = None
cnt = 0
for _ in range(n):
    a = int(input())
    array.append(a)
array.sort()
print(math.floor(sum(array)/n + 0.5))
print(array[(len(array)//2)])
dic = dict()
for i in array:  # 빈도수 구하기
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

mx = max(dic.values())
mx_dic = []

for i in dic:
    if mx == dic[i]:
        mx_dic.append(i)

if len(mx_dic) > 1:
    print(mx_dic[1])
else:
    print(mx_dic[0])
print(abs(max(array)-min(array)))