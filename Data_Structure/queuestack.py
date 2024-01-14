import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
second = list(map(int, input().split()))
third = list(map(int, input().split()))
m = int(input())
fifth = list(map(int, input().split()))
res = deque()

for i in range(n):
    if second[i] == 0:
        res.appendleft(third[i])
for j in range(m):
    res.append(fifth[j])
    print(res.popleft(), end=' ')