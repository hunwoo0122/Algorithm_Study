import sys
from collections import deque
input = sys.stdin.readline
queue = deque()
n = int(input())
for _ in range(n):
    commend = input().split()
    if commend[0] == '1':
        queue.appendleft(int(commend[1]))
    elif commend[0] == '2':
        queue.append(int(commend[1]))
    elif commend[0] == '3':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif commend[0] == '4':
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif commend[0] == '5':
        print(len(queue))
    elif commend[0] == '6':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif commend[0] == '7':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif commend[0] == '8':
        if queue:
            print(queue[-1])
        else:
            print(-1)