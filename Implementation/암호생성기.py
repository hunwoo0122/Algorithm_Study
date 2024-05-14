import sys
input = sys.stdin.readline
from collections import deque
# 테스트 케이스 수 입력
for i in range(1, 11):
    n = int(input())
    q = deque()
    password = list(map(int, input().split()))
    length = len(password)
    for k in range(length):
        q.append(password[k]) # q = [10, 6, 12, 8, 9, 4, 1, 3] password도 똑같
    while q[-1] > 0:
        for j in range(1, 6):
            q[0] -= j
            q.append(q.popleft())
            if q[-1] <= 0:
                q[-1] = 0
                break
    print("#{}".format(i), *q, end=" ")
    print()